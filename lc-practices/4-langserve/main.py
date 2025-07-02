import os

from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # Specify the OpenAI model to use
    temperature=0.7,  # Set the temperature for response variability
    max_tokens=150  # Limit the response length
)

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words")

prompt2 = ChatPromptTemplate.from_template(
    "Write me an song about {topic} with 100 words")

chain1 = prompt1 | llm
chain2 = prompt2 | llm

add_routes(
    app,
	chain1,
    path="/essay"
)

add_routes(
    app,
    chain2,
	path="/song"
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
