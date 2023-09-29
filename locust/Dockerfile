FROM python:3.11-slim

WORKDIR /locust

RUN pip install -v locust

COPY locust/locustfile.py /locust/locustfile.py

CMD ["locust", "-f", "/locust/locustfile.py"]