FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask pymysql

CMD ["python", "app.py"]
