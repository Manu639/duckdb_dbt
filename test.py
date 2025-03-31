import duckdb
import pandas as pd

# Create a DuckDB connection
con = duckdb.connect(database='my_database.duckdb')

data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Insert the DataFrame into DuckDB
result = con.execute("SELECT table_name, table_type FROM information_schema.tables").fetchall()
print(result)

result2 = con.execute("SELECT * FROM main.users_view").fetchall()

print(result2)