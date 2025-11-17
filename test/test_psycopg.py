import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")

print("Testing connection...")

try:
    conn = psycopg2.connect(url)
    print("SUCCESS: Connected to database")
    conn.close()
except Exception as e:
    print(f"ERROR: {e}")