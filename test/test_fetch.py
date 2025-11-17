from config.supabase_client import fetch_table

rows = fetch_table("employees", limit=5)
print(rows)