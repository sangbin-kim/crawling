import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date=20200319.html')

soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('ul', attrs={'class':'section_list_ranking'})

pol = results[0]
eco = results[1]
social = results[2]
life_cul = results[3]
world = results[4]
science = results[5]

record_pol = []
record_eco = []
record_social = []
record_life_cul = []
record_world = []
record_science = []


#----------------pol----------------------------------------------
record_pol = []


for pol_data in pol('li'):
    rank = pol_data.find('em').text
    url = "https://news.naver.com/"+pol_data.find('a')['href']
    title = pol_data.find('a')['title']
    section = "정치"
    record_pol.append((section,rank, title, url))


#----------------eco----------------------------------------------

record_eco = []

for eco_data in eco('li'):
    rank = eco_data.find('em').text
    url = "https://news.naver.com/"+eco_data.find('a')['href']
    title = eco_data.find('a')['title']
    section = "경제"
    record_eco.append((section,rank, title, url))


#----------------social----------------------------------------------

record_social = []

for social_data in social('li'):
    rank = social_data.find('em').text
    url = "https://news.naver.com/"+social_data.find('a')['href']
    title = social_data.find('a')['title']
    section = "사회 "
    record_social.append((section,rank, title, url))

#----------------life_cul----------------------------------------------


record_life_cul = []

for life_cul_data in life_cul('li'):
    rank = life_cul_data.find('em').text
    url = "https://news.naver.com/"+life_cul_data.find('a')['href']
    title = life_cul_data.find('a')['title']
    section = "생활/문화  "
    record_life_cul.append((section,rank, title, url))

#----------------world----------------------------------------------


record_world = []

for world_data in world('li'):
    rank = world_data.find('em').text
    url = "https://news.naver.com/"+world_data.find('a')['href']
    title = world_data.find('a')['title']
    section = "세계 "
    record_world.append((section, rank, title, url))

#----------------science----------------------------------------------


record_science = []


for science_data in science('li'):
    rank = science_data.find('em').text
    url = "https://news.naver.com/"+science_data.find('a')['href']
    title = science_data.find('a')['title']
    section = "IT/과학 "
    record_science.append((section,rank, title, url))


import pandas as pd

df_pol = pd.DataFrame(record_pol, columns=['section', 'rank', 'title', 'url'])
df_eco = pd.DataFrame(record_eco, columns=['section', 'rank', 'title', 'url'])
df_social = pd.DataFrame(record_social, columns=['section', 'rank', 'title', 'url'])
df_life_cul = pd.DataFrame(record_life_cul, columns=['section', 'rank', 'title', 'url'])
df_world = pd.DataFrame(record_world, columns=['section', 'rank', 'title', 'url'])
df_science = pd.DataFrame(record_science, columns=['section', 'rank', 'title', 'url'])

news_frame = [df_pol, df_eco, df_social, df_life_cul, df_world, df_science]
result_news_frame = pd.concat(news_frame)

result_news_frame.to_csv('200319_popular_news_by_section.csv', index=False, encoding='utf-8')
