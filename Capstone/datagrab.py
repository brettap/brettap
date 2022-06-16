from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
url = 'https://partners.amazonaws.com/search/partners/'
driver.get(url)
# navigate to page above

# find links to click on for each card
links = driver.find_element(By.CLASS_NAME, "partner-link").click
for link in links:
    #click on link, but how?
    link.click()
   

    print(name)
