# looping through first page of elements and scaping data
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas 
import math
import time
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd



options = Options()

driver = webdriver.Chrome()
base_url = 'https://partners.amazonaws.com/search/partners/?page='
page_number = 1
url = base_url + str(page_number)
driver.get(url)



# navigate to page above
time.sleep(1)
# find links to click on for each card
pagination_elements = driver.find_elements(by=By.CLASS_NAME, value='pagination-page-number')
page_list = []
for li in pagination_elements:
    page_number_li = li.find_element_by_tag_name('button').text
    if page_number_li.isdigit():
        page_list.append(int(page_number_li))

total_pages = len(page_list)

# go to customer page
# partner_details list holder
partner_details = []
pd = pandas.DataFrame()
# excel output file
output_file_name = "partners_workbookv5.xlsx"

counter = 1
links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
# total_pages = 650 # added a count of 1000, 950, 850, but only got 10 more records
try:

    while page_number <= total_pages:
        # print total pages? to see if total pages is equal to 645
        print(total_pages)
        if math.ceil(counter / 10) > 1:
            page_number = page_number + 1 # 2 changed to try to skip forward collected only 40 records
            if page_number > total_pages:
                break
            counter = 1
            driver.get(base_url + str(page_number))
            time.sleep(2)
            links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')

        links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
        link = links[(counter -1) ]
        link.click()
        

        name = driver.find_element(by=By.CLASS_NAME, value='partner-bio__header').text
        logo = driver.find_element(by=By.CLASS_NAME, value='split-panel__logo').find_element(by=By.TAG_NAME, value='img').get_attribute('src')
        partner_website = driver.find_elements(by=By.CLASS_NAME, value='nav-item').find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        desc = driver.find_element(by=By.CLASS_NAME, value='split-panel__blurb').text
        cont = driver.find_element(by=By.CLASS_NAME, value='partner__contact-btn').find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        links = driver.find_elements(by=By.CLASS_NAME, value='partner-link') # added in for no such element in 58
        aws_partner_page = driver.find_elements(by=By.CLASS_NAME, value='parnter-link').get_attribute('href')
        # print(name, logo, desc, cont)
        driver.back()
        links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
        counter = counter +1
        
        
        partner_detail = {

            "Partner Name ": name,
            "Partner Logo": logo,
            "Partner Website": partner_website,
            "Partner Description": desc,
            "Partner Contact": cont,
            "AWS Partner Page": aws_partner_page
           
          
        }
        print(partner_detail)
        partner_details.append(partner_detail)
        
except:
    print("error")

finally:
    driver.quit()
    
    df = pandas.DataFrame(partner_details)
    # print(partner_details)
    print(df)
    df.to_excel(output_file_name, sheet_name='Sheet1')

    # errors: line 30, in <module> total_pages = max(page_list) ValueError: max() arg is an empty sequence
