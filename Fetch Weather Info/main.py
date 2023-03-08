# This project utilizes the openweather API. Please make sure to get your API key.
import requests
from datetime import date
from pprint import pprint
# Pretty print module useful for converting JSON data to user-friendly readble format.

# NOTE: Enter your API Key here
API_Key = ''

city = input('Enter your city: ')
base_url = (
    f'http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}'
)
weather_data = requests.get(base_url).json()
print(f"""
---------------------------------------
Weather in {city} on {date.today()} is: 
---------------------------------------
        """)
pprint(weather_data)
