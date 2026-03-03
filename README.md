# 🚀 DB Migration Tracking with Alembic & SQLAlchemy

> A Python project demonstrating robust database migration management using Alembic and SQLAlchemy.

---

## 📖 Description
- This project showcases how to manage and track database schema changes in a PostgreSQL database using Alembic migrations with SQLAlchemy ORM models.
- It exists to provide a reproducible, version-controlled workflow for evolving database schemas in Python applications.
- It solves the problem of manual schema updates, ensuring consistency and traceability across development, staging, and production environments.

---

## 🎯 Objectives
- Enable safe, versioned schema migrations for a PostgreSQL database.
- Demonstrate best practices for Alembic migration scripts, including idempotency and rollback.
- Integrate SQLAlchemy models with Alembic for autogeneration and migration tracking.

---

## ✨ Features
- Initial schema creation and migration.
- Column renaming and index management via migrations.
- Splitting a single column into multiple columns with data transformation.
- Rollback and migration history commands.
- FastAPI integration for CRUD operations on the `users` table.

---

## 🧠 Key Concepts Demonstrated
- Alembic migration workflow (`revision`, `upgrade`, `downgrade`, `history`, `current`).
- Idempotent migration scripts (checking for column existence before adding).
- SQLAlchemy model-driven migrations.
- Environment variable-based configuration for database credentials.

---

## 🏗️ Architecture Overview

The project consists of:
- A db_migration_tracking_alembic Python package containing SQLAlchemy models, database setup, and FastAPI endpoints.
- An alembic folder with migration scripts and configuration.
- Alembic manages schema changes, while SQLAlchemy models define the database structure.

```text
DB-Migration-Tracking-Alembic/
│
│   .env
│   .gitignore
│   alembic.ini
│   poetry.lock
│   pyproject.toml
│   README.md
│
├───alembic
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│   └──versions
│        └──307456355dea_split_full_name.py
│           4550e751363e_add_index_to_mobile_number.py
│           96b254012b4b_initial_schema.py
│           98fe1d485507_add_phone_number_to_users.py
│           e796b6067c33_rename_phone_number_to_mobile_number.py
│
└───src
    └───db_migration_tracking_alembic
         └───database.py
             main.py
             models.py
             schemas.py
             __init__.py
```

---

## ⚙️ Setup Instructions

**Prerequisites**  
- Python 3.12+
- PostgreSQL database
- `pip` for installing dependencies

**Installation**  
1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your .env file with your database URL:
   ```
   DATABASE_URL=postgresql://username:password@localhost/dbname
   ```
4. Initialize Alembic:
   ```
   alembic upgrade head
   ```

---

## 🔑 Configuration

Environment variables or configuration details:  
- `DATABASE_URL`: PostgreSQL connection string (stored in .env, not in alembic.ini).

---

## ▶️ Usage

How to run the project:  
- Start the FastAPI server:
  ```
  uvicorn src.db_migration_tracking_alembic.main:app --reload
  ```
- Run Alembic migrations:
  ```
  alembic revision --autogenerate -m "your message"
  alembic upgrade head
  alembic downgrade -1
  alembic history
  alembic current
  ```

Example request (FastAPI):
```json
POST /users
{
  "full_name": "Aditya Zala",
  "email": "adityazala@gmail.com",
  "mobile_number": "1234567890"
}
```

---

## 📝 Learnings

- How to structure and manage database migrations in Python projects.
- Importance of idempotent migration scripts to avoid errors on repeated runs.
- How to keep sensitive configuration out of version control using environment variables.
- Integration of Alembic with SQLAlchemy models for seamless schema evolution.
- Using FastAPI for modern Python web APIs with database support.