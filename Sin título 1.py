# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:06:36 2018

@author: jose.molina
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:39:40 2018

@author: jose.molina
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests
from xml.etree import ElementTree
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from dateutil.relativedelta import relativedelta

import re

url = 'https://www.tripadvisor.es/Restaurants-g187514-Madrid.html#EATERY_OVERVIEW_BOX'
browser = webdriver.Chrome(r'C:\Users\Jose.Molina\Downloads\WinPython\projects\tripadvisor\chromedriver.exe')
#'/home/josemolina/programs_python/geckodriver'
browser.implicitly_wait(10)
browser.get(url)

#li id="alphabetical"
alpha = browser.find_element_by_id('alphabetical')
alpha.click()


html = BeautifulSoup(browser.page_source, 'html.parser')
table = html.find_all('div',{'data-index': re.compile(r".*")})
for row in table:
    item = row.find('a', class_='property_title')
    expediente = browser.find_element_by_id(item['id'])
            expediente.click()

print(table)
print("\n")

            #coger id de ventana actual
            #main_window = browser.cur