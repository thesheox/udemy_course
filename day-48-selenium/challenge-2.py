from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
test=driver.get('https://en.wikipedia.org/wiki/Main_Page')
# driver.implicitly_wait(10)

# number=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# number.click()


# all_portals=driver.find_element(By.LINK_TEXT,value="anyone can edit")
# all_portals.click()
# print(number.text)
# driver.quit()
# driver.quit()

search=driver.find_element(By.CSS_SELECTOR,".cdx-text-input__input")
search.send_keys("python")
search.send_keys(Keys.ENTER)


# button=driver.find_element(By.CSS_SELECTOR,"#searchform button")
# button.click()