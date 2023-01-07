from bs4 import BeautifulSoup
import requests
from pprint import pprint

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to go for billboard hot 100? Type the date in YYYY-MM-DD format: ")

response = requests.get(URL + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names]
pprint(song_list)

