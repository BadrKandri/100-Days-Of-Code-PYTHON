import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
#https://login.twilio.com/u/signup?state=hKFo2SBHVzJaZkc5QlhKWHJUZjhrZkNvUEY1cUw1WWdrbEM0eaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE8wYTlZTG1BeE1qZE5LUXgxZ3lfZkJfODVvZzE3MTB6o2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks
#visit this website to get ur: API_KEY, TWILIO_ACCOUNT_ID,AUTH_TOKEN 
api_key = "YOUR_OWM_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_ID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

weather_params = {
    #https://www.latlong.net ----> to get your city lat and lon 
    "lat": 33.573109,#for Casablanca, Morocco
    "lon": -7.589843,#for Casablanca, Morocco
    "appid": api_key, #https://openweathermap.org/api/hourly-forecast ----> visit this website to get your free api key
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
