from bs4 import BeautifulSoup as bs
import requests

url = 'https://academy.hackthebox.com/'
resp = requests.get(url)
tree = bs(resp.text, 'html.parser')
for link in tree.find_all('a'):
	print(f"{link.get('href')} --> {link.text}")