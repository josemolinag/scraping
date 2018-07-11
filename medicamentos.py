# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:49:56 2018

@author: jose.molina
"""

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
import requests
from xml.etree import ElementTree
from time import sleep

import pandas as pd
from dateutil.relativedelta import relativedelta

import re

def getvalueofnode(node):
    """ return node text or None """
    return node if node is not None else None
 
dfcols = ['codigo', 'titulo', 'f_inicio','f_fin','mensaje']
df_xml = pd.DataFrame(columns=dfcols)

url = 'https://www.aemps.gob.es/cima/publico/listadesabastecimiento.html'
browser = webdriver.Chrome(r'C:\Users\Jose.Molina\Downloads\WinPython\projects\tripadvisor\chromedriver.exe')
#browser = webdriver.Chrome(r'C:\Users\Jose.Molina\Downloads\WinPython\projects\tripadvisor\phantomjs.exe')


#'/home/josemolina/programs_python/geckodriver'
    
browser.implicitly_wait(10)
browser.get(url)

browser.implicitly_wait(10)
resuelto=browser.find_element_by_id('filtroResuelto')
resuelto.click()
sleep(2)

html = BeautifulSoup(browser.page_source, 'html.parser')
a = browser.find_elements_by_class_name('list-group-item-med')
#a = browser.find_elements_by_css_selector("div.list-group-item-med")
for i,elem in enumerate(a):
    print(i)
    browser.implicitly_wait(10)
    aux = browser.find_elements_by_class_name('list-group-item-med')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    while len(browser.find_elements_by_class_name('list-group-item-med')) > len(aux):
        aux = browser.find_elements_by_class_name('list-group-item-med')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
    for items in aux:
        
    
    
    if aux[i].get_attribute('onclick') != None:
        print(aux[i].get_attribute('onclick'))
        browser.execute_script("arguments[0].click();",aux[i])
        sleep(2)
        browser.get(browser.current_url)
        browser.execute_script('window.history.go(-1)')
        sleep(2)
        browser.get(browser.current_url)
#    