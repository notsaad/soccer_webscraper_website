import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://fbref.com/en/comps/9/Premier-League-Stats"

# html .get functions
page = requests.get(url)

# beautiful soup object
soup = BeautifulSoup(page.content, "html.parser")

print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))
    
table = soup.find('table', class_='stats_table sortable min_width force_mobilize')

# collecting data
for row in table.tbody.find_all('tr'):
    # data for each column
    columns = row.find_all('td')
    for i in range(len(columns)):
        print(columns[i].text.strip())
    # print(f"Team Name: {columns[0].text.strip()}")
    # print(f"Matches Played: {columns[1].text.strip()}")
    # print(f"Wins: {columns[2].text.strip()}")
    # print(f"Draws: {columns[3].text.strip()}")
    # print(f"Losses: {columns[4].text.strip()}")
    