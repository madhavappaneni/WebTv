from django.http import HttpResponse
from django.http import JsonResponse
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from .models import PostModel
nitc = "http://www.nitc.ac.in"
url = ('https://newsapi.org/v2/top-headlines?'
		'sources=google-news-in&'
		'apiKey=e346981c5bd74a18a9331ff4037cafd4')

def ind_news(request):
	return HttpResponse(get_ind_news())

def nitc_news(request):
	return HttpResponse(get_nitc_news())
def presentation_news(request):
	return HttpResponse(get_presentation_news())

def get_ind_news():
	try:
		indNewsArr = []
		response = requests.get(url)
		conn_string = response.json()
		articles = conn_string[u'articles']
		for i in range(1,6):
			indNewsArr.append(articles[i][u'title']+ " : " +articles[i][u'description']+" <br>") 
		return arrToStr(indNewsArr)
	except requests.ConnectionError:
		return "ConnectionError"
def get_nitc_news():
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')]
		page = opener.open(nitc)
		bsObj = BeautifulSoup(page, "html.parser")
		news = bsObj.find_all(class_='leftmenu')
		newsArr = []
		for i in range(5):
			newsArr.append(news[i].get_text()+"<br>")
		return arrToStr(newsArr)
	except urllib2.URLError as e:		
		return "URLError"

def get_presentation_news():
	presentation_array = []
	for e in PostModel.objects.all():
		presentation_array.append(str(e)+"<br>")
	return arrToStr(presentation_array)
def arrToStr(array):
	return "".join(element for element in array)



