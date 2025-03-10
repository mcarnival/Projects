#linkedin scrap
from bs4 import BeautifulSoup
import requests
import pandas as pd



dates = ['may-4-2024',
'april-27-2024',
'april-20-2024',
'april-13-2024',
'april-6-2024',
'march-30-2024',
'march-23-2024',
'march-16-2024',
'march-9-2024',
'march-2-2024',
'february-24-2024',
'february-17-2024',
'february-10-2024',
'february-3-2024',
'january-27-2024',
'january-20-2024',
'january-13-2024',
'january-6-2024',
'december-30-2023',
'december-23-2023',
'december-16-2023',
'december-9-2023',
'december-2-2023',
'november-25-2023',
'november-18-2023',
'november-11-2023',
'november-4-2023',
'october-28-2023',
'october-21-2023',
'october-14-2023',
'october-7-2023',
'september-30-2023',
'september-23-2023',
'september-16-2023',
'september-9-2023',
'september-2-2023',
'august-26-2023',
'august-19-2023',
'august-12-2023',
'august-5-2023',
'july-29-2023',
'july-22-2023',
'july-15-2023',
'july-8-2023',
'july-1-2023',
'june-24-2023',
'june-17-2023',
'june-10-2023',
'june-3-2023',
'may-27-2023',
'may-20-2023',
'may-13-2023',
'may-6-2023',
'apr-29-2023',
'apr-22-2023',
'apr-15-2023',
'apr-8-2023',
'apr-1-2023',
'mar-25-2023',
'mar-18-2023',
'mar-11-2023',
'mar-4-2023',
'feb-25-2023',
'feb-18-2023',
'feb-11-2023',
'feb-4-2023',
'jan-28-2023',
'jan-21-2023',
'jan-14-2023',
'jan-7-2023',
'dec-31-2022',
'dec-24-2022',
'dec-17-2022',
'dec-10-2022',
'dec-3-2022',
'nov-26-2022',
'nov-19-2022',
'nov-12-2022',
'nov-5-2022',
'oct-29-2022',
'oct-22-2022',
'oct-15-2022',
'oct-8-2022',
'oct-1-2022',
'sep-24-2022',
'sep-17-2022',
'sep-10-2022',
'sep-3-2022',
'aug-27-2022',
'aug-20-2022',
'aug-13-2022',
'aug-6-2022',
'jul-30-2022',
'jul-23-2022',
'jul-16-2022',
'jul-9-2022',
'jul-2-2022',
'jun-25-2022',
'jun-18-2022',
'jun-11-2022',
'jun-4-2022',
'may-28-2022',
'may-21-2022',
'may-14-2022',
'may-7-2022',
'apr-30-2022',
'apr-23-2022',
'apr-16-2022',
'apr-9-2022',
'apr-2-2022',
'mar-26-2022',
'mar-19-2022',
'mar-12-2022',
'mar-5-2022',
'feb-26-2022',
'feb-19-2022',
'feb-12-2022',
'feb-5-2022',
'jan-29-2022',
'jan-22-2022',
'jan-15-2022',
'jan-8-2022',
'jan-1-2022',
'dec-25-2021',
'dec-18-2021',
'dec-11-2021',
'dec-4-2021',
'nov-27-2021',
'nov-20-2021',
'nov-13-2021',
'nov-6-2021',
'oct-30-2021',
'oct-23-2021',
'oct-16-2021',
'oct-9-2021',
'oct-2-2021',
'sep-25-2021',
'sep-18-2021',
'sep-11-2021',
'sep-4-2021',
'aug-28-2021',
'aug-21-2021',
'aug-14-2021',
'aug-7-2021',
'jul-31-2021',
'jul-24-2021',
'jul-17-2021',
'jul-10-2021',
'jul-3-2021',
'jun-26-2021',
'jun-19-2021',
'jun-12-2021',
'jun-5-2021',
'may-29-2021',
'may-22-2021',
'may-15-2021',
'may-8-2021',

]



def extract(date):
    headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    url = f'https://www.americantop40.com/charts/top-40-238/{date}/'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup



def transform(soup, date):
    figures= soup.find_all('figure')
    for i, figure in enumerate(figures):
        track_title = figure.find('a', class_ = "track-title").text
        track_artist = figure.find('a', class_ = "track-artist").text
        wks_on_chart = figure.find('div', class_ = "track-meta").text.split()[0]
        peaks = figure.find('div', class_ = "track-meta").text.split()[1]
        item = {"date": date,
                "rank": i + 1,
                "track_title":track_title,
                "track_artist":track_artist,
                "wks_on_chart":wks_on_chart,
                "peaks":peaks,      
        }
        top40americalist.append(item)
    return
top40americalist = []



for i in dates:
    print(f"getting dates {i}")
    c = extract(i)
    transform(c,i)

df = pd.DataFrame(top40americalist)
df.head()
df.to_csv('top40americalist.csv')
len(df)


















# dates= ['may-4-2024','april-27-2024',]

# for date in dates:
#     soup = extract(date)

#     figures= soup.find_all('figure')
#     for i, figure in enumerate(figures):
#         track_title = figure.find('a', class_ = "track-title").text
#         track_artist = figure.find('a', class_ = "track-artist").text
#         wks_on_chart = figure.find('div', class_ = "track-meta").text.split()[0]
#         peaks = figure.find('div', class_ = "track-meta").text.split()[1]
#         item = {
#                 "date": date,
#                 "rank": i + 1,
#                 "track_title":track_title,
#                 "track_artist":track_artist,
#                 "wks_on_chart":wks_on_chart,
#                 "peaks":peaks,      
#         }
#         print(item)











# soup =BeautifulSoup(html_text, 'lxml')
# figures = soup.find_all('figure')




# df =[]
# for figure in figures:
#     df.append({"track_title":figure.find('a', class_ = "track-title").text,
#                "track_artist":figure.find('a', class_ = "track-artist").text,
#                "wks_on_chart":figure.find('div', class_ = "track-meta").text.split()[0],
#                "peaks":figure.find('div', class_ = "track-meta").text.split()[1] })
# df = pd.DataFrame(df)
# df











    # df.append(pd.DataFrame({"track_title":track_title,
    #                        "track_artist":track_artist,
    #                        "wks_on_chart":wks_on_chart,
    #                        "peaks":peaks}))





