import paramiko

def comando_ssh(ip, user, passwd, cmd, porta="22"):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, port=porta, username=user, password=passwd)

	_, stdout, stderr = client.exec_command(cmd)
	output = stdout.readlines() + stderr.readlines()
	if output:
		print("--- Resposta ---")
		for line in output:
			print(line.strip())

if __name__ == '__main__':
	import getpass
	# user = getpass.getuser()
	user = input('Username: ')
	password = getpass.getpass()

	ip = input('Digite o IP do servidor: ')
	port = input('Digite a porta (22 default): ')
	cmd = input('DIgite o comando: ')
	
	if port != "":
		comando_ssh(ip, user, password, cmd, port)
	else:
		comando_ssh(ip, user, password, cmd)
