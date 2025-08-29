select county, AVG(electric_range) 
from data
Group by county
order by avg(electric_range) desc
