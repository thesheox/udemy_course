import requests
import datetime as dt
MY_LAT=29.5926
MY_LONG=52.5836



parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
sunrise_time=sunrise.split("T")[1].split("+")[0]
now_time=dt.datetime.now()
print(now_time)
print(sunrise_time)

