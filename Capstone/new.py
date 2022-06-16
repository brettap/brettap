# more practice
from re import T
from bs4 import BeautifulSoup as bs
from numpy import logical_or
# from urllib.requests import urlopen
# import requests
# import contexlib
import pandas
import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = 'none'

base_link = "https://partners.amazonaws.com/search/partners/"
num_pages = math.ceil(6431 / 10)
# num_pages = 643.1

# output_file_name = "partners_workbook.xlsx"
output_file_name = "parntersv1.xlsx"

def page_suffix(page: int) -> str:
    return "?awsui.page-psf.tab.partners=" +str(page)

def full_link(page: int) -> str:
    return base_link + page_suffix(page)

if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()

        partner_infos = []

        for page in range(1, num_pages+1):
            link = full_link(page)
            print(link)
            driver.get(link)

            time.sleep(.001)

            html = driver.page_source

            soup = bs(html, "html.parser")
            partner_data = soup.find("div", "partners.find.results")


            data = partner_data.find("div", class_="card-body")
            for data in partner_data:
                #print(data)
                # print(type(data))
                name = data.find("a", class_="partner-link card-title").string
                # print(name)

                logo = data.find("div", class_="Partner Logo").string
                # print(logo)

                desc = data.find("div", class_="psf-partner-search-details-card__description").string
                # print(desc)

                # cont = data.find("")
                # print(cont)
            
            partner_info = {
                "Name": name,
                "Logo": logo,
                "Description": desc
            }
            print(partner_info)

            partner_infos.append(partner_info)
    finally:
        driver.quit();

    df = pandas.DataFrame(partner_infos)

    print(partner_infos)

    print(df)

    df.to_excel(output_file_name, sheet_name="Sheet1")










