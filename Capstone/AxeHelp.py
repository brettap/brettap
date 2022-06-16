# looping through first page of elements and scaping data
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas 
import math
import time
from time import sleep
from selenium.webdriver.chrome.options import Options


options = Options()

driver = webdriver.Chrome()
base_url = 'https://partners.amazonaws.com/search/partners/?page='
page_number = 278
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

total_pages = max(page_list)

# go to customer page
# partner_details list holder
partner_details = []
# excel output file
output_file_name = "partners_workbookv18.xlsx"

counter = 1
links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
try:
    
    while page_number <= total_pages:
        
        if math.ceil(counter / 10) > 1:
            page_number = page_number + 1
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
        logo = driver.find_element(by=By.CLASS_NAME, value='split-panel__logo').find_element_by_tag_name('img').get_attribute('src')
        desc = driver.find_element(by=By.CLASS_NAME, value='split-panel__blurb').text
        
        cont = driver.find_element(by=By.CLASS_NAME, value='more-info__location').text
        links = driver.find_elements(by=By.CLASS_NAME, value='partner-link') # added in for no such element in 58
        # print(name, logo, desc, cont)
        driver.back()
        links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
        counter = counter +1
        
        
        partner_detail = {
            "Partner Name ": name,
            "Partner Logo": logo,
            "Partner Description": desc,
            "Partner Contact": cont
        }
        print(partner_detail)
        partner_details.append(partner_detail)
except:
    print("SOMETHING WENT WRONG")


finally:
    driver.quit()
    df = pandas.DataFrame(partner_details)
    # print(partner_details)
    print(df)
    df.to_excel(output_file_name, sheet_name='Sheet1')









