from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

from bs4 import BeautifulSoup, SoupStrainer #HTML parsing
import urllib.request #aufrufen von URLs
from time import sleep #damit legen wir den Scraper schlafen
import json #lesen und schreiben von JSON-Dateien
from datetime import datetime #um den Daten Timestamps zu geben
import re #regular expressions
import os #Dateipfade erstellen und lesen

def read_products(txt):
    f = open(txt)
    return f.readlines()

def get_job(driver,url):
    
    driver.get(url)
    job={}

    job['title']= driver.find_elements(By.XPATH,'//h1[@class="o-stage__title"]')[0].text
    job['ort']= driver.find_elements(By.XPATH,'//li[@class="m-search-hit__item"]')[0].text
    job['bei']= driver.find_elements(By.XPATH,'//li[@class="m-search-hit__item"]')[1].text
    job['gebiet']= driver.find_elements(By.XPATH,'//li[@class="m-search-hit__item"]')[2].text
    job['start']= driver.find_elements(By.XPATH,'//li[@class="m-search-hit__item"]')[3].text
    job['job-nr']= driver.find_elements(By.XPATH,'//li[@class="m-search-hit__item"]')[4].text
    #job['art']= driver.find_elements(By.XPATH,'//li[@class="class="m-search-hit__item u-d-none""]')[0].text
    try:
    	a=driver.find_elements(By.XPATH,'//div[@class="o-jobad__text"]')[0]
    	job['stellenbeschreibung']=a.find_elements(By.CSS_SELECTOR,'div')[0].text
    except:
    	job['stellenbeschreibung']=''

    counter=0
    for i in a.find_elements(By.CSS_SELECTOR,'ul'):
        if counter==0:
            job['aufgabe']=i.text.replace('\n','. ')
        else:
            job['profil']=i.text.replace('\n','. ')
        counter+=1

    return job

def get_info(driver, lst):
    
    pc_info={}
    
    for url in lst:
        print('Bearbeitung beginnt ...')
        print(url)
        driver.get(url)
        pc_info[url] = get_job(driver, url)
    return pc_info
    
def pc_save(dic):
    df = pd.DataFrame(dic).T
    df.to_csv("db_jobs.csv",sep=";", encoding='utf-8-sig')
    
def get_driver():
    options = Options()
    options.headless = True # Browser not opened
    driver = webdriver.Firefox(options=options)
    #driver = webdriver.Firefox()
    return driver

jobs = read_products('db_stellen.txt')
driver = get_driver()
jobs_dic = get_info(driver,jobs)
pc_save(jobs_dic)
