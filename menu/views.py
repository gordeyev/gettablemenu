from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

from menu.models import MenuRuURLs

# Create your views here.

def home(request):
	return render(request, 'menu/index.html')

def menu_ru(request):
	context = { 'menu_ru_urls': MenuRuURLs.objects.all()}
	return render(request, "menu/menu-ru-list.html", context)










def file_to_menu_ru_urls():
	f1 = open('menuru.txt', "r")
	for one_url in f1:
		url = "http://" + one_url
		title = get_title(url)
		if title is None:
			title = '*** This page has errors!'
		print title
		p = MenuRuURLs(url=url, title=title)
		p.save()

def get_title(url_text):
	my_page = requests.get(url_text)
	soup = BeautifulSoup(my_page.text)
	return soup.title.string

