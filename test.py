import requests
from data_extraction import Weather

province_code = input("Insert the province code: ")
ine_code = input("Insert the code from the NEI (INE) of the town: ")

api = f"https://www.el-tiempo.net/api/json/v2/provincias/{province_code}/municipios/{ine_code}"
response = requests.get(api)

if response.status_code == 200:
    data = response.json()

# Importem la classe Weather
weather = Weather(data)

# Executem tots els mètodes i imprimim els resultats
print("Creation time:", weather.get_creation_time())
print("Town:", weather.get_town())
print("Province:", weather.get_province())
print("Today's date:", weather.get_today_date())
print("Altitude:", weather.get_altitude())
print("Coordinates:", weather.get_coords())
print("State of the sky:", weather.get_state_sky())
print("Actual temperature:", weather.get_actual_temp())
print("Today's min temperature:", weather.get_today_min())
print("Today's max temperature:", weather.get_today_max())
print("Actual humidity:", weather.get_actual_humidity())
print("Actual wind speed:", weather.get_actual_wind_speed())
print("Actual probability of rain:", weather.get_actual_probability_rain())
print("Actual precipitation:", weather.get_actual_precipitation())
print("Today's sunrise:", weather.get_today_sunrise())
print("Today's sunset:", weather.get_today_sunset())
print("Today's estimated precipitation:", weather.get_today_precipitation())
print("Today's probability of rain:", weather.get_today_prob_rain())
print("Today's probability of storm:", weather.get_today_prob_storm())
print("Today's snow:", weather.get_today_snow())
print("Today's probability of snow:", weather.get_today_prob_snow())
print("Today's hourly temperature:", weather.get_today_temp())
print("Today's hourly thermal sensation:", weather.get_today_thermal_sens())
print("Today's hourly relative humidity:", weather.get_today_relative_hum())
print("Today's hourly wind data:", weather.get_today_wind())
print("Today's max wind speed:", weather.get_today_max_wind())
print("Today's sky description:", weather.get_today_sky_description())
print("Tomorrow's date:", weather.get_tomorrow_date())
print("Tomorrow's sunrise:", weather.get_tomorrow_sunrise())
print("Tomorrow's sunset:", weather.get_tomorrow_sunset())
print("Tomorrow's estimated precipitation:", weather.get_tomorrow_precipitation())
print("Tomorrow's probability of rain:", weather.get_tomorrow_prob_rain())
print("Tomorrow's probability of storm:", weather.get_tomorrow_prob_storm())
print("Tomorrow's snow:", weather.get_tomorrow_snow())
print("Tomorrow's probability of snow:", weather.get_tomorrow_prob_snow())
print("Tomorrow's hourly temperature:", weather.get_tomorrow_temp())
print("Tomorrow's hourly thermal sensation:", weather.get_tomorrow_thermal_sens())
print("Tomorrow's hourly relative humidity:", weather.get_tomorrow_relative_hum())
print("Tomorrow's hourly wind data:", weather.get_tomorrow_wind())
print("Tomorrow's max wind speed:", weather.get_tomorrow_max_wind())
print("Tomorrow's sky description:", weather.get_tomorrow_sky_description())

# Comprovem si la data de la API és correcta
try:
    print("Checking API data correctness:", weather.check_all_correct())
except ValueError as e:
    print(e)