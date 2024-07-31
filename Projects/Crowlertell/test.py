import re

# Texto de exemplo que contém um número de telefone
texto = "Este é um exemplo de texto que contém um número de telefone: (11) 1234-567 55999919626, (55) 988327298"

# Expressão regular para encontrar números de telefone
padrao = r'\(?\d{2}\)?\s?\d{4,5}\-?\d{4}'

# Procurar por correspondências no texto usando a expressão regular
correspondencias = re.findall(padrao, texto)

# Exibir os resultados
print(correspondencias)