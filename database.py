from sqlalchemy import create_engine
from sqlalchemy import text
#from database import engine

DATABSE_URL = (
    "postgresql://r0n01gu:"
    "@localhost:5432/employee_db"
    "?gssencmode=disable"
)

engine = create_engine(DATABSE_URL)

def save_employee(employee):

    query = text("""
        INSERT INTO employee_processed 
        (
            emp_id, 
            name, 
            salary, 
            bonus, 
            department,
            processed_time
        )
        VALUES 
        (
            :emp_id, 
            :name, 
            :salary, 
            :bonus, 
            :department,
            NOW()
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            employee
        )
