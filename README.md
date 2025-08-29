# project-trendh

Requirements
1. python 3
2. pip modules requests pandas sqlite3 os
   pip install pandas sqlite3 os requests

3. Clone this repository
4. run ETL.py. This will:
   download census data
   connect to SQL and import the data into a database, creating a table if it doesn't exist already
   export 3 CSV files that show the trend of adoption of electric cars in Washington State.

CSV files are answering 3 questions:
(1) which cars are not eligible for tax credits
      This data shows cars that are not able to for tax credits. As there are older cars that are not as efficient as the newer cars, this could be used, along with the highest adoption by county, to determine what the consumers may purchase to regain tax credits.
   
(2) Counties that have the highest range of electric cars
      See which counties are having the largest adoption of the most fuel effecient cars, with further information can        be linked to the demographics of the county for more detailed inspection 
   
(3) which manufacturer of electric cars are most popular by county
      This is important as it shows which brand of electric cars is the most popular. This can show which companies are performing the best and which are the most preferred. Also due to electric vehicle charging type, can be used for development of charging infrastructure. 
