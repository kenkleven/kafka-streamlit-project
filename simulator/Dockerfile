FROM python:3.10-slim

WORKDIR /app

COPY producer.py .
COPY wait-for-kafka.sh .

RUN pip install --no-cache-dir kafka-python
RUN apt-get update && apt-get install -y netcat-openbsd

CMD ["./wait-for-kafka.sh"]
