# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:06:13 2018

@author: jose.molina
"""

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
 
dfcols = ['nombre', 'link', 'overall_rating','ranking','rango_precio','num_opiniones','ops_exc','ops_muybueno','ops_normal','ops_malo','ops_pesimo','punt_servicio','punt_comida','punt_calprecio','direccion','ubicacion','telefono']
df_xml = pd.DataFrame(columns=dfcols)

url = 'https://www.aemps.gob.es/cima/publico/listadesabastecimiento.html'
browser = webdriver.Chrome(r'C:\Users\Jose.Molina\Downloads\WinPython\projects\tripadvisor\chromedriver.exe')
#browser = webdriver.Chrome(r'C:\Users\Jose.Molina\Downloads\WinPython\projects\tripadvisor\phantomjs.exe')

def cargartodo(a):
    browser.implicitly_wait(10)
#    sleep(0.5)
#    resuelto=browser.find_element_by_id('filtroResuelto')
#    resuelto.click()
#    sleep(0.5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    while len(browser.find_elements_by_class_name('list-group-item-med')) > len(a):
        a = browser.find_elements_by_class_name('list-group-item-med')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
    return a
#'/home/josemolina/programs_python/geckodriver'
    
browser.implicitly_wait(10)
browser.get(url)
#html = BeautifulSoup(browser.page_source, 'html.parser')
a = browser.find_elements_by_class_name('list-group-item-med')
a = cargartodo(a)
#a = browser.find_elements_by_css_selector("div.list-group-item-med")
aux=a
for i,elem in enumerate(a):
    print(i)
    aux = cargartodo(aux)    
    if aux[i].get_attribute('onclick') != None:
        print(aux[i].get_attribute('onclick'))
        browser.execute_script("arguments[0].click();",aux[i])
        sleep(2)
        browser.get(browser.current_url)
        browser.execute_script('window.history.go(-1)')
        browser.get(browser.current_url)
        sleep(2)#    