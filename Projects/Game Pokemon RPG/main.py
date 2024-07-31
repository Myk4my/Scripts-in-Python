from Pokemon import *
from Pessoa import *
from os import system
from playsound import playsound

import pickle

def esclher_pokemon_inicial(player):
	print("{} você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!".format(player))

	pikachu = PokemonEletrico("Pikachu", level=1)
	charmander = PokemonFogo("Charmander", level=1)
	squirtle = PokemonAgua("Squirtle", level=1)
	
	print("Você possui 3 escolhas\n")
	system("echo '----- - - - - - - - -----' | lolcat -p 82 -F 0.008")
	system("echo '1 --> {}' | lolcat -p 82 -F 0.008".format(pikachu))
	system("echo '2 --> {}' | lolcat -p 82 -F 0.008".format(charmander))
	system("echo '3 --> {}' | lolcat -p 82 -F 0.008".format(squirtle))
	system("echo '----- - - - - - - - -----' | lolcat -p 82 -F 0.008")

	while True:
		escolha = int(input("\nEscolha o seu Pokemon:\n==> "))

		if escolha == 1:
			player.capturar(pikachu)
			break
		elif escolha == 2:
			player.capturar(charmander)
			break
		elif escolha == 3:
			player.capturar(squirtle)
			break
		else: print("Escolha invalida!")

def salvar(player):
	try:
		with open("database.db", "wb") as arquivo:
			pickle.dump(player, arquivo)
	except:
		print("Algo deu errado!")

def carregar():
	try:
		with open("database.db", "rb") as arquivo:
			player = pickle.load(arquivo)
			return player
	except:
		print("Jogo não encontrado!")



if __name__ == "__main__":

	player = carregar()

	# playsound('audio1.mp3', block=False)
	system("echo '------ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ------' | lolcat -p 82 -F 0.008")
	system("cat poke.txt")
	print("\n\n")
	system("figlet -w 110 ' BEM VINDO!!!' -f mono9.tlf -c | lolcat -p 16 -F 0.1 -S 65")
	system("echo '------ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ------' | lolcat -p 82 -F 0.008")
	print("\n\n")

	if not player:

		print("Olá por qual nome gostaria de ser chamado?")
		nome = input("=> ")
		player = Player(nome)
		system("echo 'Bem vindo {}' | lolcat ".format(player))
		sleep(2)
		print("Esse é um mundo habitado por POKEMONS\nSua missão é se tornar um mestre deles.\n")
		sleep(2)
		print("Capture o Máximo que conseguir e lute com seus inimigos.\n\n")
		sleep(3)
		system("echo 'SUA JORNADA COMEÇA AGORA!' | lolcat")
		print("Boa sorte!")
		sleep(2)
		system("clear")
		system("echo '------ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ------' | lolcat -p 82 -F 0.008")
		print("\n\n")
		system("figlet -w 110 ' -- - - - - - --' -f mono9.tlf -c | lolcat -p 16 -F 0.1 -S 65")
		system("echo '------ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ------' | lolcat -p 82 -F 0.008")
		print("\n\n")
		
		if player.pokemons:
			print("Percebi que já possui Pokemons")
			player.mostrar_pokemons()
		else:
			esclher_pokemon_inicial(player)
			print("Agora está pronto para explorar todo o jogo")
			system("echo 'Divirta-se!' | lolcat -p 82 -F 0.008")

		salvar(player)
	
	enemy = Inimigo("Killua")

	while True:
		system("echo '------ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ------' | lolcat -p 82 -F 0.008")
		print("\n\n")
		system("cat banner.txt")
		system("echo '------ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ------' | lolcat -p 82 -F 0.008")
		print("\n\n")
		print("Essas são suas opções\n\n")
		system("echo '----- - - - - - - - - - -----' | lolcat -p 82 -F 0.008")
		system("echo '1 --> Explorar o Mundo' | lolcat -p 82 -F 0.008")
		system("echo '2 --> Lutar contra Inimigos' | lolcat -p 82 -F 0.008")
		system("echo '3 --> Mostrar Meus Pokemons' | lolcat -p 82 -F 0.008")
		system("echo '4 --> Mostrar Cemitério' | lolcat -p 82 -F 0.008")
		system("echo '5 --> Sair do Jogo' | lolcat -p 82 -F 0.008")
		system("echo '----- - - - - - - - - - -----' | lolcat -p 82 -F 0.008")

		try:
			resp = int(input("==> "))

			if resp == 1:
				player.Explorar()
				salvar(player)
				system("clear")

			elif resp == 2:
				anenemy = Inimigo()
				player.batalhar(anenemy)
				salvar(player)
				system("clear")

			elif resp == 3:
				player.mostrar_pokemons()

			elif resp == 4:
				system("echo '----- - - - - - - - - - -----' | lolcat -p 82 -F 0.008")
				for k,v in pokemons_mortos.items():
					system("echo '{} --> {}' | lolcat -p 82 -F 0.008".format(k, v))
				system("echo '----- - - - - - - - - - -----' | lolcat -p 82 -F 0.008")
				sleep(3)

			elif resp == 5:
				break

			else:
				print("Opção inválida!")
				system("clear")
				continue

		except Exception as erro:
			print("Algo deu errado Resetando")
			print(erro)
			sleep(2)
			continue