import random as rand

from Pokemon import *
from os import system
from time import sleep


# Nome dos personagens criados aleaoriamente para seleção caso jogador não escolha o seu

NOMES = ["João", "Roberto", "Lorena", "Kilua", "Gon",
	"Ashe", "Nubia", "Morin", "Calony", "Jpitur", "Lucas", 
	"Raigen", "Garry","Luna", "Lyra", "Petrus", "Lula",
 	"Bolsonaru", "George", "Ramon", "Subi", "Cayton", "Gerundio" ]

# Nome dos Pokemons reais porem foram selecionados apeas alguns

Pokeaqua = ['Squirtle', 'Wartortle', 'Blastoise', 'Mega', 'Blastoise', 
	'Gigantamax', 'Blastoise', 'Psyduck', 'Golduck', 'Poliwag', 'Poliwhirl',
	 'Seel', 'Shellder', 'Krabby', 'Kingler', 'Gigantamax', 'Kingler']

Pokefogo = ['Charmeleon', 'Vulpix', 'Ninetales', 'Growlithe', 
	'Arcanine', 'Ponyta', 'Rapidash', 'Magmar', 'Flareon', 'Cyndaquil', 
	'Quilava', 'Typhlosion', 'Slugma', 'Magby', 'Torchic', 'Torkoal', 
	'Castform', 'Sunny', 'FormChimchar']

PokeEle = ['Pikachu', 'Gigantamax', 'PikachuRaichu', 'Voltorb', 'Eletrodo',
	 'Electabuzz', 'Jolteon', 'Pichu', 'Mareep', 'Raikou', 'Electrike', 'Manectric', 
	 'Mega Manectric', 'Blitzle', 'Zebstrika', 'Tynamo', 'Yamper', 'Boltund', 'Pincurchin', 'Regieleki']


POKEMONS = [
	PokemonFogo(rand.choice(Pokefogo)),
	PokemonEletrico(rand.choice(PokeEle)),
	PokemonAgua(rand.choice(Pokeaqua)),
]

pokemons_mortos = {}

class Pessoa:


	def __init__(self, nome=None, pokemons=[], money=100):
		self.pokemons = pokemons
		self.money = money

		if nome:
			self.nome = nome
		else:
			self.nome = rand.choice(NOMES)

	def __str__(self):
		return self.nome

	def mostrar_pokemons(self):
		if self.pokemons:
			print("\n--------------------------------------")
			print("\tPokemons de {}".format(self))
			for index,pokemon in enumerate(self.pokemons):
				print("\t|{} -- {}|".format(index+1, pokemon))
			print("--------------------------------------\n")
		else:
			print("{} não possui pokemons".format(self))

	def escolher_pokemon(self):
		if self.pokemons:
			pokeenemy = rand.choice(self.pokemons)
			print("{} escolheu {}".format(self, pokeenemy))
			return pokeenemy
		else:
			print("O jogador não possui pokemons")

	def batalhar(self, enemy):
		print("{} iniciou uma batalha com {}".format(self, enemy))
		
		enemy.mostrar_pokemons()
		pokeenemy = enemy.escolher_pokemon()
		
		pokeplayer = self.escolher_pokemon()
		
		if pokeplayer and pokeenemy:
			print("------------------------------------------")
			print("\n\n")
			system("echo '{} VS {}' | lolcat".format(pokeplayer, pokeenemy))
			sleep(2)
			print("\n\n")
			print("------------------------------------------\n\n")
			
			while True:
				if pokeplayer.vida > 0:
					pokeplayer.atacar(pokeenemy)
					sleep(2)
				else:
					print("Oh não! o vencedor é\n")
					print("-------------------------------------")
					print("O vencedor é:", pokeenemy)
					print("-------------------------------------\n")
				
				if pokeenemy.vida > 0:
					pokeenemy.atacar(pokeplayer)
					sleep(2)
				else:
					print("Parabéns!")
					print("\n\n-------------------------------------")
					print("O vencedor é:", pokeplayer)
					print("-------------------------------------\n")

				if pokeplayer.vida <=0 :
					self.Cemiterio(pokemon=pokeplayer)
					index = self.pokemons.index(pokeplayer)
					self.pokemons.pop(index)
					sleep(2)
					break

				if pokeenemy.vida <=0 :
					self.gainmoney(pokeenemy.level *100)
					enemy.Cemiterio(pokemon=pokeenemy)
					index = enemy.pokemons.index(pokeenemy)
					enemy.pokemons.pop(index)
					sleep(2)
					break
					
		else:
			print("Não é possível batallhar!")

	def gainmoney(self, quant):
		self.money += quant
		print("{} ganhou {}R$".format(self, quant))
		self.showmoney()
	
	def showmoney(self):
		print("{} Possui {}R$ em sua conta\n".format(self, self.money))

	def Cemiterio (self, pokemon):

		if self.nome in pokemons_mortos:
			pokemons_mortos[self.nome] = [pokemons_mortos[self.nome]]
			pokemons_mortos[self.nome].append(pokemon.nome)	
		else:
			pokemons_mortos[self.nome] = pokemon.nome
		
		system("echo '----- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -----' | lolcat -p 82 -F 0.008")
		system("echo 'o Pokemon {} de {} foi para o cemitério' | lolcat -p 82 -F 0.008".format(pokemon, self))
		system("echo '----- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -----' | lolcat -p 82 -F 0.008")
		sleep(3)
		system('clear')



class Player(Pessoa):

	tipo = "Player"

	def capturar(self, pokemon):
		system("figlet -w 210 'Pokebola VAI!' -f mono9.tlf | lolcat -p 16 -F 0.1")
		sleep(3)
		system("cat pokeb2.txt")
		self.pokemons.append(pokemon)
		sleep(4)
		print("{} Capturou ==> ({})".format(self, pokemon))
		system("echo '{}' | lolcat -p 16 -F 0.1; echo É seu! parabéns!".format(pokemon))
		sleep(4)
		system("clear")


	def escolher_pokemon(self):
		self.mostrar_pokemons()
		
		if self.pokemons:
			while True:
				try:
					escolha = int(input("{} Escolha o seu Pokemon para batalha\n==> ".format(self))) - 1
					pokeplayer = self.pokemons[escolha]
					print('\n\n')
					system("echo '{} EU ESCOLHO VOCÊ!!!' | lolcat".format(pokeplayer))
					sleep(2)
					print('\n\n')
					return pokeplayer
				except:
					print("Escolha inválida!")
					continue

		else:
			print("O jogador não possui pokemons")
	
	def Explorar(self):

		if rand.random() <= 0.5:
			pokevagem = rand.choice(POKEMONS)
			print("\n- - - - - - - - - - - - -  - - - - - - - -- - - - - -")
			print("Um pokemon selvagem apareceu\n{} \tTipo: {}".format(pokevagem, pokevagem.tipo))
			print("- - - - - - - - - - - - -  - - - - - - - -- - - - - - \n")
			escolha = input("Desejas capturar o pokemon?\nS/N: ")
			
			if escolha == 'S' or escolha == 's':
				if rand.random() >= 0.5:
					self.capturar(pokevagem)
					self.mostrar_pokemons()
				else:
					print("Pokebola falhou! :(\t{} Fugiu".format(pokevagem))
					sleep(2)
			else:
				print("OK boa viagem...")
				sleep(2)

		else:
			print("Essa exploração nao deu em nada\nRetornando para o menu")
			sleep(2)


class Inimigo(Pessoa):
	tipo = "Inimigo"

	def __init__(self, nome=None, pokemons=None):
		if not pokemons:
			num = rand.randint(1, 6)
			pokemons_ale = []
			for i in range(num):
				pokemons_ale.append(rand.choice(POKEMONS))

			super().__init__(nome=nome, pokemons=pokemons_ale)
		else:
			super().__init__(nome=nome, pokemons=pokemons)