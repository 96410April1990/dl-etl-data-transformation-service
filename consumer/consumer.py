import json
from kafka import KafkaConsumer
from service.transform import transform_employee
from repository.database import save_employee
from database.event_repository import (event_processed, save_processed_event)
from kafka.dlq_producer import (publish_dlq)

consumer = KafkaConsumer(
    "employee-topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    employee = message.value
    print("Received:", employee)
    event_id = employee["event_id"]
    if event_processed(event_id):
        print(
            f"Duplicate event: {event_id}"
        )
        continue

    transformed = transform_employee(
        employee
    )
    print("Transformed:", transformed)
    # save_employee(
    #     transformed
    # )
    success = process_with_retry(
        transformed
    )

    if not success:
        publish_dlq(
            employee
        )
        print("Published to DLQ")

    save_processed_event(
        event_id
    )

def process_with_retry(
        transformed,
        retries=3):
    
    for attempt in range(retries):
        try:
            save_employee(
                transformed
            )
            return True
        except Exception as e:
            print(f"Retry {attempt+1}")
    
    return False