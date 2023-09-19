# List Comprehension
# [expressão for item in iterable if condição == True]

# List comprehension que imprime os números até 10
lista = [x for x in range(10)]

print(lista)

# ------------------------------------  Lista de frutas
lista_frutas = ["banana", "abacate", "melancia", "cereja", "manga"]

# Nova lista
nova_lista = []

# Loop tradicional para buscar as palavras com letra "m"
for x in lista_frutas:
    if "m" in x:
        nova_lista.append(x)

# Mesmo resultado anterior mas com list comprehension
nova_lista2 = [x for x in lista_frutas if "m" in x]

# imprimindo as listas
print('\nNovaLista: ', nova_lista, '\nNovaLista2:', nova_lista2)


# ---------------------------------------  Dict comprehension

# ----- Dicionário de alunos e notas
dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

# Criamos um novo dicionário imprimindo os pares de chave:valor
dict_alunos_status = {k:v for (k, v) in dict_alunos.items()}
print(dict_alunos_status)

# ----- Dicionário de alunos e notas
dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

# Criamos um novo dicionário com o status: nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k:('Aprovado' if v > 70 else 'Reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)