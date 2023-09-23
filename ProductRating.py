# E-Commerce Product Rating Based On Customer Review Mining
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
from streamlit_lottie import st_lottie

global name
st.title("E-Commerce Product Rating System")
name=st.text_input("Enter product name:")

def search():
    
    print(name)
    name.strip().replace(" ","+")

    html_text = requests.get("https://www.flipkart.com/search?q="+name+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text

    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('div', class_='_4rR01T')
    prices = soup.find_all('div', class_='_30jeq3 _1_WHN1')
    ratings = soup.find_all('div', class_='_3LWZlK')
    links = soup.find_all('a', class_='_1fQZEK')
    if(len(links)==0):

        names = soup.find_all('a' , class_="s1Q9rs")
        prices = soup.find_all('div', class_="_30jeq3")
        ratings = soup.find_all('div', class_="_3LWZlK")


    if(len(links)>0):
        dict = {'Product Name':[], 'Rating':[], 'Price(₹)':[],  'Webstore':[],'Link':[]}
        for i in range(0,len(names)):
            dict['Product Name'].append(names[i].text)
            dict['Price(₹)'].append(int(prices[i].text[1:].replace(",","")))
            dict['Rating'].append(ratings[i].text+" *")
            dict['Webstore'].append("Flipkart")
            dict['Link'].append("https://www.flipkart.com"+links[i]["href"])
    else:
        dict={'Product Name':[], 'Rating':[], 'Price(₹)':[],  'Webstore':[]}
        for i in range(0,len(names)):
            dict['Product Name'].append(names[i].text)
            dict['Price(₹)'].append(int(prices[i].text[1:].replace(",","")))
            dict['Rating'].append(ratings[i].text+" *")
            dict['Webstore'].append("Flipkart")
    df = pd.DataFrame(data=dict)

    df= df.sort_values(by=['Rating'],ascending=False)
    st.write(df)
if(st.button("Search")):
        df=search()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_MzXVQG4Qi9.json")
if lottie_coding is not None:
    st_lottie(lottie_coding, height=300, key="coding")