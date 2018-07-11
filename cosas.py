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

url = 'https://www.tripadvisor.es/Restaurants-g187514-Madrid.html#EATERY_OVERVIEW_BOX'
browser = webdriver.Chrome(r'C:\Users\Jose.Molina\Downloads\WinPython\projects\tripadvisor\chromedriver.exe')
#'/home/josemolina/programs_python/geckodriver'
browser.implicitly_wait(10)
browser.get(url)

#li id="alphabetical"
alpha = browser.find_element_by_id('alphabetical')
alpha.click()
browser.implicitly_wait(10)

contador = 0
next = True
#cada vez que empieza el bucle se recorre una página entera
while next == True:
    html = BeautifulSoup(browser.page_source, 'html.parser')
    table = html.find_all('div',{'data-index': re.compile(r".*")})
    for row in table:
        item = row.find('div', class_='title')
        link = item.find('a')
        link ="https://www.tripadvisor.es"+link['href']
        browser.get(link)
        #print(link['href'])
        #elemento = browser.find_element_by_xpath('//a[@href="'+link['href']+'"]')
        #elemento.click()
        
        browser.get(browser.current_url)
        bar_html = BeautifulSoup(browser.page_source,'html.parser')
        #contenido a scrapear
        
        name = bar_html.find('h1',{'class':'heading_title'})
        rating = bar_html.find('span',{'class':'overallRating'})
        ranking = (bar_html.find('span',{'class':'header_popularity'})).find('span')
        print(ranking.text)
        precio = (bar_html.find('span',{'class':['ui_column',"is-6","price"]})).find('span')
        print(precio.text)
        #fin contenido a scrapear
        
                
        
        df_xml = df_xml.append(
            pd.Series([getvalueofnode(name.text), getvalueofnode(link), getvalueofnode(rating.text),getvalueofnode(ranking.text),getvalueofnode(precio.text),'num_opiniones','ops_exc','ops_muybueno','ops_normal','ops_malo','ops_pesimo','punt_servicio','punt_comida','punt_calprecio','direccion','ubicacion','telefono'], index=dfcols),
            ignore_index=True)
        contador += 1
        print(f'Contrato numero: {contador}')
        
        browser.execute_script('window.history.go(-1)')
    			#if (times == 0):
        browser.get(browser.current_url)
        nextpage = browser.find_element_by_css_selector('a.nav').click()

#    if class = disabled :
#        next = False
#    else:
#        
#
#    try:
#        nextpage = browser.find_element_by_css_selector('a.nav').click()
##       nextpage = browser.execute_script(" ta.restaurant_filter.paginate(this.getAttribute('data-offset'));; ta.trackEventOnPage('STANDARD_PAGINATION', 'next', '2', 0); return false;")
#        if (nextpage):
#            nextpage.click()
#        else: 
#            next = False
#    except:
#        next = False
#browser.close()
   # expediente = browser.get(link.get_attribute('href'))
    #expediente.click()
df_xml.to_excel("tripadvisor_restaurantes_madrid.xlsx", index = False)

            #coger id de ventana actual
            #main_window = browser.cur