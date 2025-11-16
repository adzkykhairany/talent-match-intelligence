# Talent Match Intelligence

Python project for analyzing talent data using Supabase and PostgreSQL.

## Setup

1. **Create virtual environment and install dependencies:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Fill in your credentials:
     ```
     SUPABASE_URL=https://your-project.supabase.co
     SUPABASE_KEY=your-key-here
     DATABASE_URL=postgresql://user:pass@host:5432/dbname
     ```

## Usage

Run the test fetch script:
```powershell
python test/test_fetch.py
```

## Project Structure

- `config/` - Database and API client configuration
  - `supabase_client.py` - Supabase client with lazy initialization
  - `postgres_connection.py` - PostgreSQL connection utilities
- `test/` - Test scripts
- `analysis/` - Analysis notebooks
