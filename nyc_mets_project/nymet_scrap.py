from bs4 import BeautifulSoup
import requests
import pandas as pd

def extract(year):
    headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    url = f'https://www.baseball-reference.com/teams/NYM/{year}.shtml'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup




def transform(soup, year):
    seasons = soup.find_all("li",class_= "result")
    for season in seasons:
        date = season.text.strip().split(sep = ",")[0]
        result = season.text.strip().split(sep = ",")[1].split()[2]
        year = year
        item = {"date":date,
                "result": result,
                "year": year}
        nymet_records.append(item)
    return

nymet_records = []


years = [2024, 2023,2022,2021,2020,2019,2018,2017,2016,2015]
for year in years:
    print(f"getting year {year}")
    c = extract(year)
    transform(c,year)

df = pd.DataFrame(nymet_records)
df.head()
df.to_csv('nymet_records.csv')
len(df)




# headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
# url = f'https://www.baseball-reference.com/teams/NYM/{2023}.shtml'
# r = requests.get(url, headers)
# soup = BeautifulSoup(r.content, 'html.parser')

# seasons = soup.find_all("li",class_= "result")
# for season in seasons:
#     date = season.text.strip().split(sep = ",")[0]
#     result = season.text.strip().split(sep = ",")[1].split()[2]
#     year = 2023
#     item = {"date":date,
#             "result": result,
#             "year": year}
#     print(item)