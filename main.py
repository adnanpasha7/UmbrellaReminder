import requests
from twilio.rest import Client

api_key = 
lat = 12.709210
lon = 78.165138

account_sid = 
auth_token = 

weather_parameters = {
    "lat": 33.019790,
    "lon": -80.177580,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to take ☔.",
        from_='+19378844366',
        to='+919108811142'
    )
    print(message.status)

