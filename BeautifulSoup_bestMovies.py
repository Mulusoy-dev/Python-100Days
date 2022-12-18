from bs4 import BeautifulSoup
import requests


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇
response = requests.get(URL)
empire_web_page = response.text


soup = BeautifulSoup(empire_web_page, "html.parser")

best_100_movies = soup.select("h3", class_="title")
movies_list = []
for tag in best_100_movies:
    movies_list.append(tag.getText())
    #print(tag.getText())

best_movies_list = movies_list[::-1]

with open("movies.txt", "w", encoding="utf8") as file:
    for text in best_movies_list:
        file.write(text)
        file.write("\n")