import gettext
from re import T
from bs4 import BeautifulSoup
import pandas as pd
import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome()


source_link = "https://partners.amazonaws.com/partners/001E000000NaBHNIA3/Cloudreach"
driver.get(source_link)
r = 1
partner_data = []

while(1):
    if __name__  == "__main__":
        try:
            name = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]').text
            logo = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[5]/div/div[2]/div[2]/img').text
            desc = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[5]/div/div[2]/div[1]').text
            cont = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[5]/div/div[3]/div[2]').text

            partner_dic = {
                "Name": name,
                "Logo": logo,
                "Description": desc,
                "Contact": cont
            }
            partner_data.append(partner_dic)
            df = pd.DataFrame(partner_data)

            r += 1
        except NoSuchElementException:
            break

df.to_csv('table.csv')
driver.close()


