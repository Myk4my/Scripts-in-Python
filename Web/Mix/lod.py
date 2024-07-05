import sys
import time


RED = "\033[31m"
GREEN = "\033[33m"
RESET = "\033[0m"

def loading_animation(message='Loading...'):
    # Loop infinito para manter a animação rodando
    j = 0
    n_m = []
    mess = message
    while True:
        # Loop para percorrer cada caractere da mensagem
        for i in range(len(mess)):
            # Alterna entre maiúsculas e minúsculas para cada caractere
            if not mess[-4].isupper():
                char = mess[i].upper()
                n_m.append(char)
            else:
                char = mess[i].lower()
                n_m.append(char)
            # Escreve o caractere na saída padrão
            sys.stdout.write(RED+char)
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

# Exemplo de uso
loading_animation()