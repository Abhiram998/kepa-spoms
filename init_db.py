
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load env vars
load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    print(f"Connecting to {DATABASE_URL}...")
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print("Connected. Reading schema file...")
            with open("new_database_schema.sql", "r") as f:
                sql_script = f.read()
            
            print("Executing schema...")
            # Split by statement (rough split, but works for this file structure)
            # or just execute_block if sqlalchemy supports it comfortably, 
            # but usually execute(text(full_script)) works for postgres with sqlalchemy if configured.
            # However, safer to just run it.
            connection.execute(text(sql_script))
            connection.commit()
            print("Database initialized successfully!")
            
    except Exception as e:
        print(f"Error initializing database: {e}")

if __name__ == "__main__":
    init_db()
