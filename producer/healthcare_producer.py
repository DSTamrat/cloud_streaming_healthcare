import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Create a Kafka producer that sends JSON messages to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Sample values for synthetic healthcare events
HOSPITAL_UNITS = ["ICU", "ER", "Cardiology", "Oncology"]
CONDITIONS = ["Sepsis", "Pneumonia", "CHF", "Stroke", "COVID-19"]

def generate_event():
    """Create one synthetic healthcare admission event."""
    return {
        "patient_id": random.randint(100000, 999999),
        "hospital_unit": random.choice(HOSPITAL_UNITS),
        "primary_condition": random.choice(CONDITIONS),
        "admission_ts": datetime.utcnow().isoformat(),
        "heart_rate": random.randint(55, 140),
        "systolic_bp": random.randint(90, 180),
    }

if __name__ == "__main__":
    topic = "healthcare_admissions_stream"
    print(f"Sending 1000 events to topic: {topic}")

    for i in range(1000):
        event = generate_event()
        producer.send(topic, event)
        print(f"{i+1}/1000 Sent:", event)
        time.sleep(1)

    print("Finished sending 1000 events.")
