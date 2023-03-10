from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
wiki = requests.get(START_URL)

soup = bs(wiki.text,'html.parser')
table = soup.find_all('table')

temp_list= []

tr = table[7].find_all('tr')

for tr in tr:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
distance =[]
mass = []
radius =[]


for i in range(1,len(temp_list)):    
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(name, distance, mass, radius)),columns=['Star_name','Distance','Mass','Radius'])
df.to_csv('dwarf_stars.csv')