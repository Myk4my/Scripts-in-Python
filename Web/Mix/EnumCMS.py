import contextlib
import os
import queue
import requests
import sys
import threading
import time

RED = "\033[31m"
GREEN = "\033[33m"
RESET = "\033[0m"


FILTERED = ['.jpg', '.gif', '.png', '.css', '.js']
site = "https://wordpress.org/showcase"
THREADS = 10
STOP = False

answers = queue.Queue()
web_paths = queue.Queue()

def get_paths():
	for root, _, files in os.walk('.'):
		for fname in files:
			if os.path.splitext(fname)[1] in FILTERED:
				continue
			path = os.path.join(root, fname)
			if path.startswith('.'):
				path = path[1:]
			#print(path)
			web_paths.put(path)

@contextlib.contextmanager
def chdir(path):
	"""
	On enter, change directory to specified path.
	On exit , change directory back to original
	"""
	this_dir = os.getcwd()
	os.chdir(path)
	try:
		yield
	finally:
		os.chdir(this_dir)

def test_remote():
	while not web_paths.empty():
		path = web_paths.get()
		url = f"{site}{path}"
		time.sleep(2)
		resp = requests.get(url)
		if resp.status_code == 200:
			answers.put(url)
			#print(f"Found URL = {url}\n")

def loading_animation():
    # Loop para manter a animação rodando
    j = 0
    n_m = []
    mess = 'Loading...'

    # Loop para percorrer cada caractere da mensagem
    while not STOP:
	    for i in range(len(mess)):
	        # Alterna entre maiúsculas e minúsculas para cada caractere
	        if not mess[-4].isupper():
	            char = mess[i].upper()
	            n_m.append(char)
	        else:
	            char = mess[i].lower()
	            n_m.append(char)
	        # Escreve o caractere na saída padrão
	        sys.stdout.write(RED+char+RESET)
	        # Força a saída padrão a ser atualizada
	        sys.stdout.flush()
	        # Pausa por um curto período de tempo
	        time.sleep(0.1)
	    mess = ''.join(n_m)
	    n_m.clear()
	    chars = [47, 45, 92, 124]
	    sys.stdout.write(f'{GREEN}[{chr(chars[j])}]{GREEN}')
	    if j == 3:
	        j = 0
	    else:
	        j +=1
	    sys.stdout.write('\r')
	    sys.stdout.flush()

def how_to():
	print("""How to use the script:
		FIRST download de CMS to enumerate,
		than place the full path as argument to the script to enumerate all folders and files
		and select the number of threads to use (default=10).
		Obs: you can also filter the extensions 
		wanted/not wanted in the FILTERED variable\n""")

	print(f"""Examples:\n\n{sys.argv[0]} /full/path/to/cms/\n{sys.argv[0]} /full/path/to/cms/ 15\n""")

def run():
	global STOP
	anim = threading.Thread(target=loading_animation)
	mythreads = []

	print(f"Spawning {THREADS} threads\n")
	anim.start()
	for i in range(THREADS):
		#print(f"Spawning thread {i}")
		t = threading.Thread(target=test_remote)
		mythreads.append(t)
		t.start()
	for thread in mythreads:
		thread.join()
	STOP = True
	anim.join()
	print(f"{RED}killing Threads{RESET}\n")


if __name__ == '__main__':
	if len(sys.argv) < 2:
		how_to()
		sys.exit()
	elif len(sys.argv) == 3:
		THREADS = int(sys.argv[2])
	with chdir(sys.argv[1]):
		get_paths()

	print('Starting the Enumeration...\n')

	run()
	with open('Resultado.txt', 'w') as file:
		while not answers.empty():
			file.write(f"{answers.get()}\n")
	print("Feito!")

