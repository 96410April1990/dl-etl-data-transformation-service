from sqlalchemy import text
from db import engine

def event_processed(event_id):
    query = text("""
        SELECT COUNT(*)
        FROM processed_events
        WHERE event_id=:event_id
    """)

    with engine.begin() as conn:
        result = conn.execute(
            query,
            {
                "event_id": event_id
            }
        )

        return result.scalar() > 0
    
def save_processed_event(event_id):
    query = text("""
        INSERT INTO processed_events
        (
                 event_id,
                 processed_at
        )
        VALUES
        (
                 :event_id,
                 NOW()
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "event_id": event_id
            }
        )
