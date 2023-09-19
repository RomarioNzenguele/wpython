
# Exemplo de matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# imprimindo a matriz
for linha in matriz:
    for elemento in linha:
        # Usando end="  " para imprimir na mesma linha
        print(elemento, end="  ")
    print()  # Imprimir uma quebra de linha após cada linha da matriz

print('\n')

# imprimindo matriz de *
tamanho = 4
for i in range(0, tamanho):
    for j in range(0, tamanho):
        print('*', end=" ")  # Usando end="  " para imprimir na mesma linha
    print()  # Imprimir uma quebra de linha após cada linha da matriz
