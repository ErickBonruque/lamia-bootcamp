from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('h2')

for movie in movies:
    name = movie.find('a')
    ano = movie.find('span', class_='subtle start-year')

    if name and ano:
        moreInfo = name.get('href')
        ano_int = int(ano.text.strip("()"))

        if ano_int == 2020:
            print(f'\nFilme: {name.text} Ano: {ano.text}')
            print(f'Link: {moreInfo}\n')
    else:
        print('Alguma informação não encontrada para este filme')
