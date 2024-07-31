from os import system

AGENDA = {}
resp = None

def mostrar_contatos():
	if AGENDA:
		for contato in AGENDA:
			busca_contato(contato)
	else:
		print("Agenda Vazia\n")

def busca_contato(nome):
	if nome in AGENDA:
		print("-------------------------------")
		print("Nome:", nome)
		print("Telefone:", AGENDA[nome]["tel"])
		print("Email:", AGENDA[nome]["email"])
		print("ende:", AGENDA[nome]["ende"])
		print("-------------------------------\n")
	else:
		print("contato", nome, "não encontrado!")

def incluir_editar_contato(nome):
	tel = input("Telefone: ")
	email = input("Email: ")
	ende = input("Endereço: ")
	if nome in AGENDA:
		print("\nContato [", nome, "]\nEditado com sucesso\n")
	else:
		print("\nContato [", nome, "]\nAdicionado com sucesso\n")
	
	AGENDA[nome] = {
		'tel': tel,
		'email': email,
		'ende': ende,
	}
	salvar()

def continuar ():
	print("Desejas continuar?")
	resp = input("[Digite qualquer tecla para SIM e N para NÃO] => ")

	if resp == 'N' or resp == 'n':
		quit()

	system('clear')

def exportar_contatos(export):
	try:
		with open(export, 'w') as agenda:
			for contato in AGENDA:
				tel = AGENDA[contato]['tel']
				mail = AGENDA[contato]['email']
				ende = AGENDA[contato]['ende']
				agenda.write("{},{},{},{}\n".format(contato, tel, mail, ende))
					
	except:
		print("ERROR")

def importar_contatos(arquivo):
	try:
		with open(arquivo) as arq:
			lista = arq.readlines()

			for linha in lista:
				palavras = linha.split(',')			
				AGENDA[palavras[0]] = {
					'tel': palavras[1],
					'email': palavras[2],
					'ende': palavras[3],
				}		
	except IndexError:
		pass
	except Exception as error:
		print(error)

def salvar():
	exportar_contatos('database.csv')
	with open('database.csv','rw') as file:
		for line in file:
			if not line.isspace():
				file.write(line)

def carregar():
	importar_contatos('database.csv')

carregar()

while True:
	print("---------------------------------")
	print("|\tPrograma Agenda\t\t|")
	print("---------------------------------\n")
	print("---------------------------------")
	print("|\t      Menu\t\t|")
	print("---------------------------------")
	print("[1] = \tIncluir contato\t\t|")
	print("[2] = \tEditar contato\t\t|")
	print("[3] = \tExcluir contato\t\t|")
	print("[4] = \tMostar contatos\t\t|")
	print("[5] = \tExportar em arquivo\t|")
	print("[6] = \tImportar em arquivo\t|")
	print("---------------------------------")
	print('O que você gostaria de fazer\n')

	try:
		resp = int(input("==> "))
		
		if resp == 1:
			nome = input("Digite o nome do contato: ")
			try:
				AGENDA[nome]
				print("Contato já existe! Não é possível adicioná-lo\n")
				continuar()
				continue
			except:
				incluir_editar_contato(nome)
				busca_contato(nome)

		elif resp == 2:
			nome = input("Digite o nome do contato: ")
			
			if nome not in AGENDA:
				print("O contato [",nome,"] não está na agenda")
				continuar()
				continue
			else:
				incluir_editar_contato(nome)
				busca_contato(nome)

		elif resp == 3:
			print("Qual contato desejas remover?")
			contato = input("Nome: ")
			if contato in AGENDA:
				print("Removendo contato...")
				AGENDA.pop(contato)
				salvar()
			else:
				print("Não é possível remover o contato [", contato, "]\n")
				print("Motivo: Contato não existe na Agenda\n")

		elif resp == 4:
			print("Mostrando todos os contatos na agenda atualmente\n")
			mostrar_contatos()
	
		elif resp == 5:
			nome = input("Nome do arquivo a ser exportado: ")
			
			if '.csv' not in nome:
				nome += '.csv'
			exportar_contatos(nome)

		elif resp == 6:
			arquivo = input("Digite o nome do CSV que desejas importar: ")
			if '.csv' not in arquivo:
				arquivo += '.csv'
			importar_contatos(arquivo)
	
		else:
			print("Opção inválida!\n")

	except ValueError as erro:
		print("Erro de valor, tente digitar um númeor\n")

	continuar()