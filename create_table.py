import lancedb
import os

db_path = "./lancedb_data"
print(f"Database will be created at: {os.path.abspath(db_path)}")

db = lancedb.connect(db_path)

table_name = "recipes"
try:
    db.drop_table(table_name)
    print(f"Dropped existing table: {table_name}")
except Exception:
    print(f"Table {table_name} didn't exist")

print("Table setup complete! Run main.py next.")
