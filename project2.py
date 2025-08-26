import sqlite3
import pandas as pd
connection = sqlite3.connect('company.db') #connection to the db
cursor = connection.cursor() #object to run queries

df = pd.read_csv('test.csv')
#print(df.info())

name_table = 'Companies'

columns_with_types = ", ".join([f"{col.replace(' ', '_')} TEXT" for col in df.columns]) # Eg: page_id TEXT, name TEXT, urslug TEXT, ...
create_table_query = f"CREATE TABLE IF NOT EXISTS {name_table} ({columns_with_types})"

cursor.execute(create_table_query)
connection.commit()
connection.close()

