import sys
import requests	

def urls(arquivo):
	url2 = sys.stdin.read().splitlines()

	boas = []
	ruins = []

	for url in url2:
		try:
			resp = requests.get(url)
			if resp.status_code == 200:
				boas.append(url)
		except Exception as erro:
			ruins.append(url)
			continue

	with open(arquivo, 'w') as file:
		file.write('\n'.join(boas))
	print(f"Urls salvas em [{arquivo}]")

arquivo = 'filtradas'
urls(arquivo)