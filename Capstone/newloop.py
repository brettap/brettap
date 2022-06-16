# looping through first page of elements and scaping data
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas 
import time
from time import sleep
# from selenium.webdriver.chrome.options import Options


# options = Options()

driver = webdriver.Chrome()
base_url = 'https://partners.amazonaws.com/search/partners/?page='
page_number = 1
driver.get(base_url + str(page_number))
# navigate to page above
time.sleep(2)
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
output_file_name = "partners_workbookv_2.xlsx"

# links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
try:

    while page_number <= total_pages:
        driver.get(base_url + str(page_number))
        time.sleep(3)
        links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')
        number_of_links = len(links) if len(links) <= 10 else 10
        
        for index in range(number_of_links):
            links[index].click()
            name = driver.find_element(by=By.CLASS_NAME, value='partner-bio__header').text
            logo = driver.find_element(by=By.CLASS_NAME, value='split-panel__logo').find_element_by_tag_name('img').get_attribute('src')
            desc = driver.find_element(by=By.CLASS_NAME, value='split-panel__blurb').text
            cont = driver.find_element(by=By.CLASS_NAME, value='more-info__location').text
           
            partner_detail = {
            "Partner Name ": name,
            "Partner Logo": logo,
            "Partner Description": desc,
            "Partner Contact": cont
            }
            print(partner_detail)
            partner_details.append(partner_detail)
            driver.back()
            # time.sleep(1)
            links = driver.find_elements(by=By.CLASS_NAME, value='partner-link')

        page_number = page_number + 1
               
except Exception as error:
    print(error)

finally:
    driver.quit()
    df = pandas.DataFrame(partner_details)
    # print(partner_details)
    print(df)
    df.to_excel(output_file_name, sheet_name='Sheet1')
