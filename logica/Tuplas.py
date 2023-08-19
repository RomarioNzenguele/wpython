# Nota: Collections em Python possuem tipagem dinamica

# Tuplas: sao listas inalteraveis, ou seja, n suporta a inclusao/exclusao de elementos
# suportam varios metodos e/ou propriedades aplicadas as listas desde que estas n adulterem a sua estrutura

paises = ()  # criando uma tupla vazia
paises = ("Angola", "Rwanda", "Congo", "Namibia")

print(paises, "\nTamanho:", len(paises))
print(paises[2])  # acessando um elemento

# convertendo em lista
paises = list(paises)
print(type(paises))

# convertendo novamente em tupla
paises = tuple(paises)
print(type(paises))