FROM python:3.11-slim

COPY requirements.txt .

RUN apt update

RUN apt install libgomp1 -y

RUN pip install -r requirements.txt && rm requirements.txt

EXPOSE 80

COPY ./api /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]