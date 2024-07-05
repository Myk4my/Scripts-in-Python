from io import BytesIO
from lxml import etree

import requests


def func():
	for i in range(1,5):
		print('\n')

url = 'https://nostarch.com'
r = requests.get(url)
content = r.content

func()
print("APÓS O REQUEST\n\n",content)

parser = etree.HTMLParser()
func()
print("APÓS O ETREE\n\n",parser)

content = etree.parse(BytesIO(content), parser=parser)
func()
print('APÓS O PARSE DO ETREE\n\n',content)
for link in content.findall('//a'):
	print(f"{link.get('href')} ---> {link.text}")

