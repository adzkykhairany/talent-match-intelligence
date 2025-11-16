from supabase import create_client, Client
from dotenv import load_dotenv
import os
from typing import Any

load_dotenv()

_supabase_client: Client | None = None


def get_supabase_client() -> Client:
    """Get or create Supabase client from environment variables."""
    global _supabase_client
    if _supabase_client is None:
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        if not url or not key:
            raise RuntimeError(
                "SUPABASE_URL and SUPABASE_KEY environment variables must be set. "
                "Add them to .env file"
            )
        _supabase_client = create_client(url, key)
    return _supabase_client


def fetch_table(table_name: str) -> Any:
    """Fetch all records from a Supabase table."""
    supabase = get_supabase_client()
    response = supabase.table(table_name).select("*").execute()
    return response.data