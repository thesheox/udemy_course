from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
test=driver.get('https://python.org')
# driver.implicitly_wait(10)
date_name={}
dates=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget a")
for n in range(len(dates)):
    if "More" not in names[n].text:
        date_name[n]={
            "name":names[n].text,
            "date":dates[n-1].text
        }
print(date_name)
# driver.quit()
driver.quit()