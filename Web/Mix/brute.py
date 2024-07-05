import queue
import requests
import threading
import sys

AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0"
EXTENSIONS = ['.php','.txt','.inc','.bak']
TARGET = "http://testphp.vulnweb.com"
THREADS = 10

def get_words(resume=None):

	def extended_words(word):
		if '.' in word:
			words.put(f'/{word}')
		else:
			words.put(f'/{word}/')

		for extension in EXTENSIONS:
			words.put(f'/{word}{extension}')

	with open(WORDLIST) as f:
		raw_words = f.read()

	found_resume = False
	words = queue.Queue()
	for word in raw_words.split():
		if resume is not None:
			if found_resume:
				extended_words(word)
			elif word == resume:
				found_resume = True
				print(f'Resuming wordlist from: {resume}')
		else:
			#print(word)
			extended_words(word)

	return words	

def dir_bruter(words):
	headers = {'User-Agent': AGENT}
	while not words.empty():
		url = f'{TARGET}{words.get()}'
		try:
			r = requests.get(url, headers=headers)
		except requests.exceptions.ConnectionError:
			sys.stderr.write('x');sys.stderr.flush()
			continue

		if r.status_code == 200:
			print(f'\nSucess [{r.status_code}: {url}]')
		elif r.status_code == 404:
			sys.stderr.write('.');sys.stderr.flush()
		else:
			print(f'{r.status_code} ==> {url}')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(f"Usage: {sys.argv[0]} wordlist\n")
	WORDLIST = sys.argv[1]
	words = get_words()
	print("Enumerando...")
	#sys.stdin.readline()
	for _ in range(THREADS):
		t = threading.Thread(target=dir_bruter, args=(words,))
		t.start()
