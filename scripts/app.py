from bs4 import BeautifulSoup, SoupStrainer #HTML parsing
import urllib.request #aufrufen von URLs
from time import sleep #damit legen wir den Scraper schlafen
import json #lesen und schreiben von JSON-Dateien
from datetime import datetime #um den Daten Timestamps zu geben
import re #regular expressions
import os #Dateipfade erstellen und lesen
import pandas as pd #Datenanalyse und -manipulation
import requests
#import urllib.request

def car(url):
#    URL=urllib.request.Request(url_car)
    page = requests.get(url)
    car = BeautifulSoup(page.content, 'html.parser')

    car_dict = {}                
    #car = BeautifulSoup(urllib.request.urlopen(URL).read(),'lxml')
    try:
        car_dict["Marke"] =  car.find("span",attrs={"class":"StageTitle_boldClassifiedInfo__L7JmO"}).text
    except:
        pass
    try:
        car_dict["Modell"] = car.find("span",attrs={"class":"StageTitle_model__pG_6i"}).text
    except:
        pass
    try:
        car_dict['Variante']=car.find("div",attrs={"class":"StageTitle_modelVersion__Rmzgd"}).text
    except:
        pass
    try:
        car_dict['Preis']=car.find("span",attrs={"class":"StandardPrice_price__X_zzU"}).text#.replace("€ ","").replace(".","").split(',')[0])
    except:
        pass
    try:
        car_dict['Ort']=car.find('a',attrs={"class":"scr-link"}).text
    except:
        pass
    
    #car_dict['Bundesland']=""
    
    for i in car.find_all("div",attrs={"class":"VehicleOverview_itemContainer__Ol37r"}):
        #car_dict[car.find_all("div",attrs={"class":"VehicleOverview_itemTitle__W0qyv"})[i].text]=
        car_dict[i.find('div',attrs={'class':"VehicleOverview_itemTitle__W0qyv"}).text]=i.find('div',attrs={'class':"VehicleOverview_itemText__V1yKT"}).text
    for i in car.find_all("div",attrs={"class":"DetailsSection_detailsSection__2cTru"}):
        for j in i.find_all("dl",attrs={"class":"DataGrid_defaultDlStyle__969Qm"}):
            for k in range(len(j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"}))):
            
                if j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"})[k].text=="Komfort" or j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"})[k].text=="Unterhaltung/Media" or j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"})[k].text=="Sicherheit" or j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"})[k].text=="Extras":                
                    ausstattung = []
                    ausstattung.append(j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"})[k].text)
                    for l in j.find_all("dd",attrs={"class":"DataGrid_defaultDdStyle__29SKf"})[k]:
                        ausstattung.append([t.text for t in l.find_all("li")])
                    for m in range(0,len(ausstattung)-1,2):
                        car_dict[str(ausstattung[m])]=ausstattung[m+1]
                else:
                    car_dict[j.find_all("dt",attrs={"class":"DataGrid_defaultDtStyle__yzRR_"})[k].text]=j.find_all("dd",attrs={"class":"DataGrid_defaultDdStyle__29SKf"})[k].text
    try:
        car_dict['Fahrzeugbeschreibung_html']=car.find('div',attrs={"class":"SellerNotesSection_content__S5suY"})
    except:
        pass
    try:
        car_dict['Preisbewertung']=car.find('div',attrs={"class":"Price_priceCategoryContainer__8xcSY"}).text
    except:
        pass
    #TODO: get price categories by click_event
    
    try:
        car_dict['Unternehmen']=car.find_all('div',attrs={"class":"RatingsAndCompanyName_dealer__HTXk_"})[0].find('div').text
        car_dict['Straße_PLZ_Ort']=car.find_all('a',attrs={"class":"scr-link Department_link__6hDp5"})[0].text
    except:
        pass
    try:
        car_dict['Rating_Anzahl']=car.find_all('span',attrs={"class":"DealerRatings_ratingsText__jQfKc"})[0].text.split(' ')[0]
        car_dict['Rating']=car.find_all('span',attrs={"class":"DealerRatings_recommendationsText__kn0Gj"})[0].text.split(' ')[0].replace('(','')
    except:
        pass
    try:
        car_dict['Kontakt']=car.find_all('span',attrs={"class":"Contact_contactName__MFXhS"})[0].text
        car_dict['Telefon']=car.find_all('a',attrs={"class":"scr-link Contact_link__hRROM"})[0].text
    except:
        pass
    try:
        car_dict[car.find_all('a',attrs={"class":"scr-link StockList_link___HKPA"})[0].text]=car.find_all('a',attrs={"class":"scr-link StockList_link___HKPA"})[0].get('href')
        car_dict[car.find_all('a',attrs={"class":"scr-link DealerLinks_bold__coH8c"})[1].text]=car.find_all('a',attrs={"class":"scr-link DealerLinks_bold__coH8c"})[1].get('href')
        car_dict[car.find_all('a',attrs={"class":"scr-link DealerLinks_bold__coH8c"})[0].text]=car.find_all('a',attrs={"class":"scr-link DealerLinks_bold__coH8c"})[0].get('href')
    except:
        pass
    
    
    return car_dict

def multi_car(url_cars,k):
    multiple_cars_dict = {}
    car_URLs = []
    #path_to_visited_urls = "data/visited/visited_urls.txt"
    #if not os.path.isfile(path_to_visited_urls):
    #    with open(path_to_visited_urls,"w") as file:
    #        file.write("")
    #with open(path_to_visited_urls,'r',encoding='utf-8') as file:
    #    visited_urls = [line for line in file]
    
    try:
        url=url_cars
        only_a_tags = SoupStrainer("a")
        soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser', parse_only=only_a_tags)
        for link in soup.find_all("a"):
            if r"/angebote/" in str(link.get("href")):
                #print(link.get("href"))
                car_URLs.append(link.get("href"))
        #print(len(car_URLs))

    except Exception as e:
        print("Übersicht: " + str(e) +" "*50, end="\r")
        pass

    car_URLs_unique = [car for car in list(set(car_URLs))]

    if len(car_URLs_unique)>0:
        for i in range(len(car_URLs_unique)):
            URL="https://www.autoscout24.de"+car_URLs_unique[i]
            multiple_cars_dict[URL]=car(URL)
            #visited_urls.append(URL)

    if len(multiple_cars_dict)>0:
        df = pd.DataFrame(multiple_cars_dict).T
        #df.to_csv("Mercedes_"+str(k)+".csv",sep=";", encoding='utf-8-sig')
        return df

marke=[#'volkswagen','mercedes-benz','bmw','skoda','audi','ford','opel',
'toyota','renault','seat']

def get_page_n(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
    
    try:
    	return max([int(t.text) for t in soup.find_all('li',attrs={'class':'pagination-item'})])
    except:
    	return 0


for j in marke:
    for k in range(2010,2024,1):
        url="https://www.autoscout24.de/lst/"+j+"?doorfrom=4&doorto=5&fregfrom="+str(k)+"&fregto="+str(k)+"&sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&fuel=B&powertype=kw&emclass=4&ensticker=4&ocs_listing=include&search_id=23ly56064xb"
        page_n=get_page_n(url+'&page=1')
        print(j+" Jahr "+str(k)+": Seite:"+str(page_n))
        #print('Für '+str(k)+'-'+'( mit '+ str(page_n) +' Seiten) wird der Vorgang gestartet:')
        if page_n<20:
            if page_n==1:
                print('Seite '+str(1)+' wird bearbeitet...')
                url2=url+"&page=1"
                d_f=multi_car(url2,1)
                d_f.to_csv("Dataset_"+j +"_"+str(k)+".csv",sep=";",encoding="utf-8")
            else:
                df2=[]
                for i in range(1,page_n+1):
                    start_i=datetime.now()
                    print('   Seite '+str(i)+' wird bearbeitet...')
                    url2=url+"&page="+str(i)
                    d_f=multi_car(url2,i)
                    df2.append(d_f)
                results=pd.concat(df2)
                results.to_csv("Dataset_"+j+"_"+str(k)+".csv",sep=";",encoding="utf-8")
        else:
            for l in range(1,6):
                url2=url+"&pe_category="+str(l)
                page_n=get_page_n(url2+'&page=1')
                print("Jahr "+str(k)+": Page"+str(page_n)+", Cat:"+str(l))
                if page_n==1:
                    url2=url2+"&page="+str(1)
                    d_f=multi_car(url2,1)
                    d_f.to_csv("Dataset_"+j +"_"+str(k)+"_Cat"+str(l)+".csv",sep=";",encoding="utf-8")
                elif page_n<20:
                    df3=[]
                    for i in range(1,page_n+1):
                        start_i=datetime.now()
                        print('   Seite '+str(i)+' wird bearbeitet...')
                        url3=url2+"&page="+str(i)
                        d_f=multi_car(url3,i)
                        df3.append(d_f)
                        #print('   Die Bearbeitung der Seite '+str(i)+' hat '+str(datetime.now()-start_i)+' gedauert.')
                    results=pd.concat(df3)
                    results.to_csv("Dataset_"+j+"_"+str(k)+"_Cat"+str(l)+".csv",sep=";",encoding="utf-8")
                else:
                    for t in [1,5,6]:
                        print("Jahr "+str(k)+": Page"+str(page_n)+", Cat:"+str(l)+", Body:"+str(t))
                        url3=url2+"&body="+str(t)
                        page_n=get_page_n(url3+'&page=1')
                        print("Jahr "+str(k)+": Page"+str(page_n)+", Cat:"+str(l) +", Body:"+str(t))
                        if page_n==1:
                            url3=url3+"&page="+str(1)
                            d_f=multi_car(url3,1)
                            d_f.to_csv("Dataset_"+j +"_"+str(k)+"_Cat"+str(l)+".csv",sep=";",encoding="utf-8")
                        elif page_n<20:
                            df3=[]
                            for i in range(1,page_n+1):
                                start_i=datetime.now()
                                print('   Seite '+str(i)+' wird bearbeitet...')
                                url4=url3+"&page="+str(i)
                                d_f=multi_car(url4,i)
                                df3.append(d_f)
                                #print('   Die Bearbeitung der Seite '+str(i)+' hat '+str(datetime.now()-start_i)+' gedauert.')
                            results=pd.concat(df3)
                            results.to_csv("Dataset_"+j+"_"+str(k)+"_Cat"+str(l)+"Body:"+str(t)+".csv",sep=";",encoding="utf-8")
                        else:
                            print("Seitenzahl mehr oder gleich 20 ...")

