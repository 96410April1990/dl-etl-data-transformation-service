import json
from kafka import KafkaConsumer
from transform import transform_employee
from database import save_employee

consumer = KafkaConsumer(
    "employee-topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    employee = message.value
    print("Received:", employee)
    transformed = transform_employee(
        employee
    )
    print("Transformed:", transformed)
    save_employee(
        transformed
    )