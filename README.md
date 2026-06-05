# DL ETL Data Transformation Service

A Python-based ETL (Extract, Transform, Load) service that consumes employee records from a Kafka topic, applies data transformations, and persists the results to a PostgreSQL database.

## Overview

The service listens to the `employee-topic` Kafka topic, transforms each incoming employee record (normalising fields, applying a 10% salary uplift, and computing a bonus), then inserts the processed record into the `employee_processed` PostgreSQL table.

## Project Structure

```
.
├── app.py                    # Application entry point (stub)
├── main.py                   # Alternate entry point
├── requirements.txt          # Python dependencies
├── config/
│   └── config.py             # Configuration (stub)
├── consumer/
│   └── consumer.py           # Kafka consumer loop
├── model/                    # Data models (stub)
├── repository/
│   └── database.py           # SQLAlchemy database layer
└── service/
    └── transform.py          # Employee transformation logic
```

## Transformation Logic

For each employee message received from Kafka, the service:

| Input field   | Output field   | Rule                            |
|---------------|----------------|---------------------------------|
| `empId`       | `emp_id`       | Direct mapping                  |
| `name`        | `name`         | Converted to uppercase          |
| `salary`      | `salary`       | Increased by 10%                |
| —             | `bonus`        | 10% of the uplifted salary      |
| `department`  | `department`   | Direct mapping                  |

## Prerequisites

- Python 3.9+
- Apache Kafka (with `employee-topic` topic created)
- PostgreSQL with an `employee_db` database

### PostgreSQL Table

```sql
CREATE TABLE employee_processed (
    emp_id      TEXT,
    name        TEXT,
    salary      NUMERIC,
    bonus       NUMERIC,
    department  TEXT,
    processed_time TIMESTAMP
);
```

## Setup

1. **Clone the repository and navigate to the project root:**

   ```bash
   cd dl-etl-data-transformation-service
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database connection** in `repository/database.py`:

   ```python
   DATABASE_URL = "postgresql://<user>:<password>@<host>:5432/employee_db?gssencmode=disable"
   ```

## Running the Service

Run the consumer from the **project root** using the module flag so that all package imports resolve correctly:

```bash
python3 -m consumer.consumer
```

> Running `python3 consumer/consumer.py` directly will fail with a `ModuleNotFoundError` because Python won't include the project root on `sys.path`.

## Dependencies

| Package           | Purpose                        |
|-------------------|--------------------------------|
| `kafka-python`    | Kafka consumer client          |
| `pandas`          | Data manipulation utilities    |
| `sqlalchemy`      | Database ORM / connection pool |
| `psycopg2-binary` | PostgreSQL driver              |
