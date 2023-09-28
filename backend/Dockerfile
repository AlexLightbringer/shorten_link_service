FROM python:3.11-slim

WORKDIR /app

COPY backend/app.py /app/app.py

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]