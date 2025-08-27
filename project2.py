import sqlite3
import pandas as pd
import requests

##Downloading file
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
filename = "test.csv"

response = requests.get(url)
with open(filename, "wb") as f:
    f.write(response.content)

connection = sqlite3.connect('test.db')

df = pd.read_csv('test.csv', header=0)
##SQL Table generation & Import

# table name
name_table = 'data'

#header row

df.columns = [col.replace(" ","_").lower() for col in df.columns]

#inserting rows
df.to_sql(name_table, connection, if_exists='replace', index=False)

connection.commit()
connection.close()

#Selecting the Top 100 fuel efficient cars
sqlitefile = "test.db"
conn = sqlite3.connect(sqlitefile)
c = conn.cursor()
f = open('selecttop100.sql','r')
sql = f.read()

df = pd.read_sql_query(sql,conn)
df.to_csv("selecttop100.csv", index=False)
