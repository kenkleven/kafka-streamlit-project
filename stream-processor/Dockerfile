FROM python:3.10-slim

WORKDIR /app

COPY stream_app.py .

RUN pip install --no-cache-dir faust-streaming

CMD ["faust", "-A", "stream_app", "worker", "-l", "info"]
