import requests
from twilio.rest import Client

api_key = '****'
account_sid = '****'
auth_token = '****'

param = {
    'lat': 51.507351,
    'lon': -0.127758,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=param)
response.raise_for_status()
print(response.status_code)
print(response.json())
weather_details = response.json()
weather_conditions = weather_details["hourly"][:12]
print(weather_conditions)
# for i in range(10):
#     weather_conditions.append(weather_details["hourly"][i]["weather"][0]["id"])
#
will_rain = False
for hour_data in weather_conditions:
   condition_code = hour_data["weather"][0]["id"]
   if int(condition_code)<700:
       will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an 🌂",
        from_='*******',
        to='********'
    )
    print(message.status)




