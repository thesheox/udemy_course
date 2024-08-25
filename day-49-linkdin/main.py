from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3944224089&keywords=python&origin=BLENDED_SEARCH_RESULT_NAVIGATION_JOB_CARD&originToLandingJobPostings=3997233493%2C3944224089%2C3944224063")
time.sleep(2)
button=driver.find_element(By.CSS_SELECTOR,value=".nav__button-secondary")
button.click()
time.sleep(2)
username=driver.find_element(By.ID,value="username")
password=driver.find_element(By.ID,value="password")
username.send_keys("thesheox.sd@gmail.com")
password.send_keys("Shayan616114")
submit=driver.find_element(By.CSS_SELECTOR,value=".btn__primary--large ")
submit.click()
input("dgdgdg")
time.sleep(2)
apply=driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button")
apply.click()
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
phone.send_keys("123456789")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button--primary")
submit_button.click()