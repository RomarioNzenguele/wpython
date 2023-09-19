# # Definindo uma funcao
# def getMedia(n1, n2):
#     media = (n1+n2)/2
#     return media

# def getMedia(n1, n2):  # Reduzindo as linhas
#     return (n1+n2)/2

# def getMedia(n1, n2): return (n1+n2)/2  # Reduzindo as linhas
 

# Transformando a funcao getMedia em lambda
getMedia = lambda n1, n2: (n1+n2)/2

print(getMedia(12,8))

# lambda sem argumentos
x, y = 12, 19
getSoma = lambda : x+y

print(getSoma())

# definindo uma funcao anonima dentro de uma outra funcao
def getProduto(x):
  return lambda y : x*y

dobro = getProduto(2)
quadruplo = getProduto(4)

print(dobro(3))
print(quadruplo(3))