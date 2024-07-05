from bs4 import BeautifulSoup as bs
from urllib import *
from sys import exit
from urllib.parse import urljoin

import requests


urls_visitadas = set()

def spider(url, keyword):
	try:
		resp = requests.get(url)
	except Exception as error:
		print(f"[-] Ocorreu um erro {error}\n")
		print("Saindo do programa...")
		exit(1)

	if resp.status_code == 200:
		soup = bs(resp.content, 'html.parser')
		a_tag = soup.find_all('a')
		url2 = []

		for tag in a_tag:
			href = tag.get("href")
			if href is not None and href != "":
				url2.append(href)
			#print(url2)

		for link in url2:
			if link not in urls_visitadas:
				urls_visitadas.add(link)
				url_join = urljoin(url, link)
				if keyword in url_join:
					print(f"Link => {url_join}")
					spider(url_join, keyword)

url = input("Digite a url que deseja scrapar: ")
keyword = input("Digite a palava chave a procurar: ")
spider(url, keyword)