from bs4 import BeautifulSoup
import requests
url = 'https://news.ycombinator.com/news'
response=requests.get(url)
# print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
links=[link.get("href") for link in soup.select(".titleline a") if "?" not in link.get("href")]
titles=[title.getText() for title in soup.select(".titleline a") if "." not in title.getText()]
scores=[int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
print(scores)
print(titles)
print(links)
max_index=scores.index(max(scores))

print(titles[max_index])
print(links[max_index])
print(scores[max_index])






