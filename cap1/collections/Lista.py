# Nota: Collections em Python possuem tipagem dinamica

# List (Lista)
# indexacao (o indice comeca sempre em 0);
paises = []  # criando uma lista vazia
paises = ["Angola", "Rwanda", "Congo", "Namibia"]
print(paises[2])
print("tipo: ", type(paises))
print("Listagem inicial: ", paises)  # imprimindo a lista

# actualizando um item
# print("\nUpdate Congo -> South Africa:\n * ", paises)
paises[2] = "South Africa"

# eliminando um item
del paises[3]
print("\nExclusao da Namibia:\n * ", paises)
paises.remove("Rwanda")
print("\n Removendo Rwanda:\n * ", paises)

# limpando a lista
# paises.clear() ou paises = {}


# adicionando um item
paises.append("Zambia")  # append add apenas um item
# extend add mais do que um item
paises.extend(["Niger", "Zimbabwe", "Cabo Verde"])
print("\nAdicionando com extend:\n * ", paises)

# adicionando em uma posicao especifica
paises.insert(1, "Egipto")
print("\nAdicionando com insert no index 1:\n * ", paises)

# Quantos items tem a lista
print("\nTotal de Itens:", len(paises))

# Retornando o index
# print("Index de Angola:", paises.index("Angola"))
# print("Index de Angola:", paises.index(paises[0]))

# Verificando a existencia de um item com o operador in
item = "Angola"
print("\nExiste {} na lista? R:".format(item), item in paises)

# Ordenando
paises.sort()
print("\n***\nLista Ordenada:", paises)
# Revertendo
paises.reverse()
print("\nLista Reversa:", paises)

# Criando uma lista aninhada
listas = [["Azul, Verde, Laranja"], [2010, 2011, 2015, 2020]]

# retornando o maior ano. Usar min para o inverso
print("\nRetornando o maior ano:", max(listas[1]))

# Concatenando listas
lista1, lista2 = ["Abacate", "Banana", "Cajú"], [
    "Figo", "Abacaxi", "Morango", "Maçã"]

print("\n*** \nLista1: ", lista1, "\nLista2:", lista2)
lista = lista1+lista2
print("\nLista concatenada:", lista)
