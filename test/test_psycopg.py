import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")

print("Testing:", url)

try:
    conn = psycopg2.connect(url)
    print("SUCCESS: Connected to Supabase PostgreSQL")
except Exception as e:
    print("ERROR OCCURRED:", e)