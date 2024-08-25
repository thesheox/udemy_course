from bs4 import BeautifulSoup
import  lxml
with open("website.html", errors='ignore') as file:
    contents=file.read()

soup=BeautifulSoup(contents,"html.parser")
# print(soup.prettify())
# print(soup.title.string)
# print(soup.a)
# print(soup.li)
# print(soup.p)

# all_a_tags=soup.find_all(name="a")
# all_li_tags=soup.find_all(name="li")
# all_p_tags=soup.find_all(name="p")
#
# for tag in all_a_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading=soup.find(name="h1",id="name")
# print(heading.getText())


# section_heading=soup.find(name="h3",class_="heading")
# print(section_heading.getText())

company_url=soup.select_one("p a")
print(company_url)


name=soup.select_one("#name")
print(name)



heading=soup.select(".heading")
print(heading)