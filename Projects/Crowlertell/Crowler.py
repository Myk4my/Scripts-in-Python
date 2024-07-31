import requests
from bs4 import BeautifulSoup

domain = "https://django-anuncios.solyd.com.br/"
url = "https://django-anuncios.solyd.com.br/automoveis"


def buscar(url):
	try:
		resposta = requests.get(url)

		if resposta.status_code == 200:
			return resposta.text
		else:
			print("Errinho básico")
	except Exception as erro:
		print(erro,"Erro ao fazer requisição")

def parsing(resposta_html):
	try:
		return BeautifulSoup(resposta_html, 'html.parser')

	except Exception as er:
		print("Erro ao fazer Parsing HTML", er)

def encontrar_links(soup):
	links = []
	cards_pai = soup.find("div", class_="ui three doubling link cards")
	cards = cards_pai.find_all("a", class_="card")

	for card in cards:
		link =  card['href']
		links.append(link)

	return links

resp = buscar(url)
if resp:
	soup = parsing(resp)
	if soup:
		links = encontrar_links(soup)
		for i in links:
			print(i)