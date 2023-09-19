# MANIPULACAO DE ARQUIVOS csv


caminho = 'W:/Treinamento/PythonDSA/arquivos/arq2.csv'

f = open(caminho, 'r')
data = f.read()

print(data)