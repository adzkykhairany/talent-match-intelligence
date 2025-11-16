from config.supabase_client import fetch_table

rows = fetch_table("dim_areas")
print(rows)