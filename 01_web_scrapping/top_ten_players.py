from bs4 import BeautifulSoup
import requests
import lxml

base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"

page = requests.get(base_url)
# print(type(page))
# print(page.status_code)


# Verify we had a successful get request webpage call
if page.status_code == requests.codes.ok:

    # print(page.text)
    # get the whoel webpage in beautiful soup formate
    bs = BeautifulSoup(page.text, 'lxml')
    # print(bs)

    # find smth you specify in the html
    # bs.find('table')
    wikitable = bs.find('table', 'wikitable')
    rows = wikitable.find_all('tr')
    top_ten_players = rows[-10:]
    data = {
        'Year': [],
        'Country': [],
        'Player': [],
        'Team/Club': []
    }
    for i in range(10):
        player = top_ten_players[i]

        name = player.find('a')['title']

        team = player.find_all('a')[-2].text

        country = str(player.find_all('span')[1]).split('title=')[1]
        country = country.strip().split('>')[0]

        year = str(player.find_all('td'))
        year = year.split('>')[1].split('\n')[0]
        if year:
            data['Year'].append(year)
        else:
            data['Year'].append("None")
        if team:
            data['Team/Club'].append(team)
        else:
            data['Team/Club'].append('None')
        if country:
            data['Country'].append(country)
        else:
            data['Country'].append('None')
        if name:
            data['Player'].append(name)
        else:
            data['Player'].append('None')
print(data)

import pandas as pd

df = pd.DataFrame(data=data, columns=['Year', 'Country', 'Player', 'Team/Club'])

df.index = df.index + 1

print(df)

df.to_csv('top_ten_palyers.csv', sep=',', encoding='utf-8', index=False)
