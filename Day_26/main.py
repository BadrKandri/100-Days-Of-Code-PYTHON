import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data=response.text
soup = BeautifulSoup(data, 'html.parser')

film_list=[]
tags=soup.find_all(name= 'h3', class_ = "title")
for tag in tags:
    film_title=tag.get_text()
    film_list.append(film_title)
film_list.reverse()
with open(file='My_Film_List.txt', mode="w", encoding="utf-8")as file:
    for film in film_list:
        file.write(film + '\n')
print('all data stored on: My_Film_List.txt')
