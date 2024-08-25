import requests
from bs4 import BeautifulSoup
year=input("which year do you want to travel into? type the date in this format YYYY-MM-DD")
url=f"https://billboard.com/charts/hot-100/{year}"
response=requests.get(url).text
soup=BeautifulSoup(response,"html.parser")
titles=soup.select("li ul li h3")

song_names=[title.getText().strip() for title in titles if ":" not in title.getText().strip()]
print(song_names)