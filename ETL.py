import sqlite3
import pandas as pd
import requests
import os

current_directory = os.getcwd()
export1 = "Top 100 Performing Electric Vehicles"
export2 = "Cars Not Eligible for Tax Credits"

##Downloading file
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
filename = "test.csv"

print("Attemping download of", url)
response = requests.get(url)
print(response) 

with open(filename, "wb") as f:
   f.write(response.content)



connection = sqlite3.connect('test.db')
print("connecting to database for import")
df = pd.read_csv('test.csv', header=0)
##SQL Table generation & Import

# table name
name_table = 'data'

#header row

df.columns = [col.replace(" ","_").lower() for col in df.columns]

#inserting rows
print("importing..")
df.to_sql(name_table, connection, if_exists='replace', index=False)

connection.commit()
connection.close()

#Selecting the Top 100 fuel efficient cars
sqlitefile = "test.db"
conn = sqlite3.connect(sqlitefile)
c = conn.cursor()
f = open('counties_with_highest_range_average.sql','r')
sql = f.read()

df = pd.read_sql_query(sql,conn)
df.to_csv("counties_with_highest_range_average.csv", index=False)

print("export of", export1, "complete, saved in", current_directory)

#Cars Not Eligible for Credits
sqlitefile = "test.db"
conn = sqlite3.connect(sqlitefile)
c2 = conn.cursor()
f2 = open('carsnoteligibleforcredits.sql','r')
sql = f2.read()

df2 = pd.read_sql_query(sql,conn)
df2.to_csv("carsnoteligibleforcredits.csv", index=False)
print("export of", export2, "complete, saved in", current_directory)

#data frame1
export3 = "Largest Manufacturer by County.csv"
query = """WITH MakeCounts AS (
  SELECT
    county,
    make,
    COUNT(*) AS make_count,
    ROW_NUMBER() OVER (PARTITION BY county ORDER BY COUNT(*) DESC) AS rn
  FROM data
  where county is not NULL
  GROUP BY
    county,
    make
)
SELECT
  county,
  make,
  make_count
FROM MakeCounts
WHERE
  rn = 1;"""

data_frame = pd.read_sql(query, conn)
data_frame.to_csv(export3, index=False)
print("Exported", export3, "successfully")
