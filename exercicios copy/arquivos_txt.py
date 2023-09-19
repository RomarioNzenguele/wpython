# MANIPULACAO DE ARQUIVOS
# 1- Abertura do file no modo desejado:
#       - 'r': leitura
#       - 'w': escrita
#       - 'a': escrita (acrescentar dados)
#  ex: arquivo = open('caminho/file.txt', 'r')
# 2- Execucao do metodo desejado
#       - read(), read(numero_caracteres): leitura   =>   seek(0,0): para retornar ao inicio da leitura
#       - write(): leitura nos modos 'w' e 'a'

caminho1 = 'W:/Treinamento/PythonDSA/arquivos/arq1.txt'


# Leitura
'''
arquivo = open(caminho1, "r")

print(arquivo.read(20)) 
print(arquivo.read())  

arquivo.close()
'''

# Escrita
arquivo = open(caminho1, "w")

arquivo.write('Pythonnnn!')
arquivo.close()

arquivo = open(caminho1, 'r')

print(arquivo.read())

arquivo.close()

# Acrescentando dados
arquivo = open(caminho1, 'a')
arquivo.write(' Eh uma grande linguagem de programacao.')

arquivo = open(caminho1, 'r')
print(arquivo.read())
close()