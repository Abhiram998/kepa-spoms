
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import CreateTable
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def dump_schema():
    if not DATABASE_URL:
        print("DATABASE_URL not found in .env")
        return

    try:
        engine = create_engine(DATABASE_URL)
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        print("-- Auto-generated schema dump")
        print("CREATE EXTENSION IF NOT EXISTS pgcrypto;")
        print("")

        for table in metadata.sorted_tables:
            # Generate CREATE TABLE statement
            create_stmt = CreateTable(table).compile(engine)
            print(f"{create_stmt};")
            print("")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dump_schema()
