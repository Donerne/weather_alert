import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

# Guelph lat long locations
weather_params = {
    'lat': 43.544804,
    'lon': -80.248169,
    'appid': api_key,
    'cnt': 4
}

# some other lat long location
#  47.376888
# 8.541694

response = requests.get(OWM_Endpoint, params=weather_params)

response.raise_for_status()

weather_forecasts = []
weather_description = []

weather = response.json()['list'][0]['weather']

for i in range(0, 4):
    weather_data = response.json()['list'][i]['weather'][0]["id"]
    weather_desc = response.json()['list'][i]['weather'][0]["description"]
    weather_forecasts.append(weather_data)
    weather_description.append(weather_desc)

for rain_check, description in zip(weather_forecasts, weather_description):
    client = Client(account_sid, auth_token)
    if rain_check < 700:

        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"Take an umbrella. Weather description: {description}",
            # from_='+17753207011',
            to="whatsapp:+16473939783")

        # print(f"Take an umbrella. Weather description: {description}")

        print(message.status)


