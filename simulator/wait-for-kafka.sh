#!/bin/sh
set -e

echo "Waiting for Kafka to be ready..."

while ! nc -z kafka 9092; do
  sleep 1
done

echo "Kafka is up ! Starting producer..."
exec python producer.py
