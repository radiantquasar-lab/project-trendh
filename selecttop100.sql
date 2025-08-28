select model_year, make, model, electric_vehicle_type, [clean_alternative_fuel_vehicle_(cafv)_eligibility], electric_utility, county
from data
where model_year BETWEEN 2010 and 2015
and [clean_alternative_fuel_vehicle_(cafv)_eligibility] not like '%clean%'
order by model_year asc
LIMIT 100