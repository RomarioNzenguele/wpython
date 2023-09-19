# Definindo uma funcao
def rir():
    print('\nAhahahahahahah\n')


def getIdade(idade):  # passando paramentros
    print(f'O estudante possui {idade} anos.\n')


def getMedia(nota1, nota2):  # Função media
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print("Media: ", (nota1+nota2)/2)


# Chamando a funcao
rir()

getIdade(20)

getMedia(14, 10)
