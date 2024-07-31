import json
import sys

import requests as req

URL_ALL = 'https://restcountries.com/v2/all'
URL_name = 'https://restcountries.com/v2/name/'


def requisicao(url):
	try:
		resposta = req.get(url)

		if resposta.status_code == 200:
			return resposta.text
	except:
		print("Erro ao fazer requisição em: ", url)

def parsing(texto_da_resposta):
	try:
		return json.loads(texto_da_resposta)
	except:
		print("Erro ao fazer parsing!")

def contagem_de_paises(paises):
	print("Existem atualmente:", len(paises), "Países no mundo")

def listagem_de_paises(paises):
	for pais in paises:
		print(pais['name'])

def populacao(pais):
	respostas = requisicao(URL_name + pais)

	if respostas:
		lista_de_paises = parsing(respostas)

		if lista_de_paises:
			for pais in lista_de_paises:
				print("{}: População {} e moeda(s) {}".format(pais['name'], pais['population'], pais['currencies'][0]['name']))
		else:
			print("País não encontrado")



if __name__ == "__main__":

	if len(sys.argv) == 1:
		print("Ben vindo ao sistema de paises")
		print("python main.py <ação> <nome do pais>")
		print("Ações diposníveis: populaçao, contagem_de_paises,")
	
	else:
		arg1 = sys.argv[1]

		if arg1 == "populaçao":
			populacao(sys.argv[2])

		elif arg1 == 'contagem_de_paises':
			contagem_de_paises(parsing(requisicao(URL_ALL)))