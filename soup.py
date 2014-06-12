import requests
from bs4 import BeautifulSoup


def get_title(url_text):
	my_page = requests.get(url_text)
	soup = BeautifulSoup(my_page.text)
	return soup.title.string


print get_title('http://menu.ru/places/menu/place/636615')