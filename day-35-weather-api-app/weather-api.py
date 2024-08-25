
import requests

end_point="https://api.openweathermap.org/data/2.5/forecast"
api_key="c6e325e91c50952a39ada080878540f3"


weather_params={
    "lat":-33.8688,
    "lon":151.2093,
    "appid":api_key,
    "exclude":"current,minutely,daily"

}
response=requests.get(end_point,params=weather_params)

weather=response.json()["list"][:24]
city=response.json()["city"]["name"]
print(city)
hour=20
rain=False
for day in weather:

    code=day["weather"][0]["id"]
    if code<800:
        rain=True



if rain:
    from twilio.rest import Client

    account_sid = 'ACdda55115b8855ac064aa65dc118799b1'
    auth_token = '03becdf4438a3a26211407e521dcf987'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+19787092299',
        body='it will rain',
        to='+989173929711'
    )

    print(message.sid)


MY_LAT=29.5926
MY_LONG=52.5836