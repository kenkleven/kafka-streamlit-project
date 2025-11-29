import json
import time
import streamlit as st
from kafka import KafkaConsumer
import pandas as pd

st.set_page_config(page_title="Visites > 30s", layout="wide")
st.title("Dashboard Temps Réel Kafka – Visites > 30 secondes")

consumer = KafkaConsumer(
    "long_visits",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

placeholder = st.empty()
data = []

while True:
    for msg in consumer:
        value = msg.value
        data.append(value)

        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])

        with placeholder.container():
            st.line_chart(df.set_index("date")["duree"])
            st.dataframe(df.tail(10))

        time.sleep(1)
