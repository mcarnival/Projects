import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


def extract(page):
    headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    url = f'https://www.cars.com/shopping/results/?deal_ratings[]=great&deal_ratings[]=good&deal_ratings[]=fair&dealer_id=&include_shippable=false&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&monthly_payment=&page={page}&page_size=20&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip='
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
        
def transform(soup):
    cars = soup.find_all('div', class_="vehicle-card ep-theme-hubcap")
    for car in cars:
        try:
            title = car.find('h2', class_="title").text.strip()
        except:
            title = ''
        try:
            deal_rating = car.find('button',class_ = 'vehicle-badging ep-theme-hubcap').text.strip().split(sep ='\n')[0]
        except:
            deal_rating = ''
        try:
            mileage = car.find('div', class_="mileage").text.strip()
        except:
            mileage = ''
        try:
            price = car.find('div', class_="price-section price-section-vehicle-card").text.strip()
        except:
            price = ''
        try:
           stock_type = car.find('p', class_ = 'stock-type').text.strip()
        except:
            stock_type = ''
        try:
            location = car.find('div', class_ ="miles-from").text.strip()
        except:
            location = ''
        item = {'title': title,
            'deal_rating':deal_rating,
            'mileage':mileage,
            'price':price,
            'stock_type':stock_type,
            'location':location}
        carlist.append(item)
    return

page = np.arange(1,10)
carlist =[]
for i in page:
    c = extract(i)
    transform(c)

df = pd.DataFrame(carlist)

df.to_csv('carlist.csv')

len(df)


# page =1
# headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
# url = f'https://www.cars.com/shopping/results/?deal_ratings[]=great&deal_ratings[]=good&deal_ratings[]=fair&dealer_id=&include_shippable=false&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&monthly_payment=&page={page}&page_size=20&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip='
# r = requests.get(url, headers)
# soup = BeautifulSoup(r.content, 'html.parser')
# car = soup.find('div', class_="vehicle-card ep-theme-hubcap")
# price = car.find('div', class_="price-section price-section-vehicle-card").text.strip()
# print(price)

from tqdm import tqdm
import time


carlist =[]
# Simulate a long-running operation
for i in tqdm(page, desc="Processing"):
    c = extract(i)
    transform(c)
    
pd.DataFrame(carlist)