select city, county, model_year, make, electric_vehicle_type, electric_utility, [clean_alternative_fuel_vehicle_(cafv)_eligibility]
from data
where model_year between 2010 and 2025
and [clean_alternative_fuel_vehicle_(cafv)_eligibility]  like '%not eligible%'
AND city IS NOT NULL
and county IS NOT NULL
AND electric_vehicle_type IS NOT NULL
AND electric_utility IS NOT NULL

order by city ASC, model_year ASC