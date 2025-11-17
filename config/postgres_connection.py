from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

_engine: Engine | None = None


def get_engine() -> Engine:
    """Get or create database engine from DATABASE_URL environment variable."""
    global _engine
    if _engine is None:
        url = os.getenv("DATABASE_URL")
        if not url:
            raise RuntimeError(
                "DATABASE_URL environment variable is not set. "
                "Add it to .env file (e.g., postgresql://user:pass@host:5432/dbname)"
            )
        _engine = create_engine(url)
    return _engine


def run_sql(query: str, params=None) -> pd.DataFrame:
    """Execute RAW SQL di Supabase Postgres and return results as DataFrame."""
    engine = get_engine()
    return pd.read_sql_query(query, engine, params=params)
