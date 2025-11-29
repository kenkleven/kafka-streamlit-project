import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

users = [
    {"id": 1, "nom": "Alice"},
    {"id": 2, "nom": "Bob"}
]

while True:
    user = random.choice(users)
    data = {
        "id": user["id"],
        "nom": user["nom"],
        "duree": random.randint(5, 60),  # durée visite
        "date": datetime.utcnow().isoformat()
    }
    print("Envoi :", data)
    producer.send("visits", data)
    producer.flush()
    time.sleep(2)
