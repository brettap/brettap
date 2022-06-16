# wedriver waiting
# looping through first page of elements and scaping data
from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

driver = webdriver.Chrome()
url = 'https://partners.amazonaws.com/search/partners/'
driver.get(url)

partner_details = []

# navigate to page above
time.sleep(3)
# find links to click on for each card
links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')

# go to customer page
#links = driver.find_element(by=By.XPATH, value='//*[@id="search-results-tab-container-tabpane-partners"]/div[4]/div[1]/div[1]/div[1]/a').click()
# partner_details list holder
partner_details = []
# excel output file
Workbook = xlsxwriter.Workbook('partners_workbook.xlsx')
worksheet = Workbook.add_worksheet()


# output_file_name = "partners_workbookv1.xlsx"

counter = 0
while counter < len(links):
    time.sleep(1)
    link = links[counter]
    
    link.click()
    
    name = driver.find_element(by=By.CLASS_NAME, value='partner-bio__header').text
    logo = driver.find_element(by=By.CLASS_NAME, value='split-panel__logo').find_element_by_tag_name('img').get_attribute('src')
    desc = driver.find_element(by=By.CLASS_NAME, value='split-panel__blurb').text
    cont = driver.find_element(by=By.CLASS_NAME, value='more-info__location').text
    print(name, logo, desc, cont)
    driver.back()
    links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
    counter = counter +1
    time.sleep(2)

    partner_detail = {
        "Partner Name ": name,
        "Partner Logo": logo,
        "Partner Description": desc,
        "Partner Contact": cont
    }
    print(partner_detail)
    partner_details.append(partner_detail)



df = pd.DataFrame(partner_details)
print(partner_details)
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
print(df)



    


 
    
    
    
    
    
    
    
