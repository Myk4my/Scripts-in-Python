import random as rand
from os import system


class Pokemon:

	def __init__(self, especie, level=None, nome=None):
		self.especie = especie
		self.level = level

		if level:
			self.level = level
		else:
			self.level = rand.randint(1,100)

		if nome:
			self.nome = nome
		else:
			self.nome = especie

		self.ataque = self.level*5
		self.vida = self.level*10

	def __str__(self):
		return "{}|>({}|{})".format(self.nome, self.level, self.vida)

	def atacar(self, pokemon):
		ataque = rand.randint(0, self.ataque)
		pokemon.vida = pokemon.vida - ataque
		print("{} perdeu {}".format(pokemon, ataque))

class PokemonEletrico(Pokemon):
	tipo = "Elétrico"
	
	def atacar(self, enemy):
		system("echo '{} Laçou um raio do trovão /´-~´-~~´/ em {}' | lolcat -p 82 -F 0.008".format(self, enemy))
		super().atacar(enemy)

class PokemonFogo(Pokemon):
	tipo = "Flamejante"
	
	def atacar(self, enemy):
		system("echo '{} Laçou uma bola de fogo (~~~) em {}' | lolcat -p 82 -F 0.008".format(self, enemy))
		super().atacar(enemy)

class PokemonAgua(Pokemon):
	tipo = "Aquático"

	def atacar(self, enemy):
		system("echo '{} Laçou um jato de agua em ~~> {}' | lolcat -p 82 -F 0.008".format(self, enemy))
		super().atacar(enemy)

