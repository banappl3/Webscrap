from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def read_products(txt):
    f = open(txt)
    return f.readlines()

def get_product_info(driver, lst):
    
    pc_info={}
    
    for url in lst:
        print(url)
        print('Bearbeitung beginnt ...')
        driver.get(url)
        pc_info[url] = get_pc(driver, url)
    return pc_info
    
def pc_save(dic):
    df = pd.DataFrame(dic).T
    df.to_csv("MediaM_notebooks.csv",sep=";", encoding='utf-8-sig')
    
def get_pc(driver, url):
    driver.get(url)
    #time.sleep(5)
    #---------------------- Javascript
    #last_height = driver.execute_script("return document.body.scrollHeight")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    erfolg=False

    while not erfolg:
        try:
            #WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="StyledButton-sc-140xkaw-1 efqYpB"]'))).click()
            #element = driver.find_element(By.XPATH, "//*[contains(text(),'Prozessor-Taktfrequenz mit Turbo')]")
            #driver.execute_script("arguments[0].scrollIntoView(true);", element)
            #button = driver.find_element(By.XPATH,"//button[@type='button' and @class='StyledLinkButton-sc-1drhx1h-1 yxevN StyledExpandLink-ea56b7-1 PSoGB']")
            #button.click()
            erfolg=True
        except:
            pass
    #driver.execute_script("arguments[0].click();", button)

    pc={}
    pc['title']= driver.find_elements(By.XPATH,'//div[@class="StyledPdpHeader-rkspnd-0 kEKdPu"]')[0].text
    pc['preis']= driver.find_elements(By.XPATH,'//span[@class="BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 LmjzB WholePrice-sc-1r6586o-7 gGcmMB"]')[0].text

    for i in driver.find_elements(By.XPATH,'//tbody[@class="StyledTableBody-v8xzh9-0 gIYkFT"]'):#[0].text
        for j in i.find_elements(By.CSS_SELECTOR,'tr'):
            #for k in j:
    #        print(j.text)
            pc[j.find_element(By.CSS_SELECTOR, 'span').text]=j.find_elements(By.CSS_SELECTOR, 'td')[1].text
    return pc


products = read_products('products.txt')
#print(products)

options = Options()
options.headless = True # Browser not opened
driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()

prod_dic = get_product_info(driver,products)
pc_save(prod_dic)

# url="https://www.mediamarkt.de/de/product/_acer-aspire-5-a515-57-50aa-mit-tastaturbeleuchtung-notebook-mit-156-zoll-display-intelr-coretm-i5-prozessor-16-gb-ram-512-gb-ssd-intel-iris-xe-grafik-steel-gray-2839062.html"
#get_pc(driver, url)
