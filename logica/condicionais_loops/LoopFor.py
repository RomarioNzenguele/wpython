# LOOP For

# Imprimindo valores de uma tupla
cor_tp = ('Azul', 'Laranja', 'Verde')
for i in cor_tp:
    print(i)

print("\n ***")

# Imprimindo numeros de 1 a 10
for contador in range(1, 11):
    print(contador)

print("\n ***")

# Imprimindo cada caracter de uma String
for caracter in 'I Hate Python!':
    print(caracter)

print("\n ***\n")


# Verificando azul nas tuplas

cor_tp = ('Azul', 'Laranja', 'Verde')
cor_tp2 = ('Cinza', 'Marrom')

# Loop externo
for i in cor_tp:
    # Loop interno
    for j in cor_tp2:
        # Condicional
        if i == 'Azul' or j == 'Azul':
            print("Cor Azul encontrada em pelo menos uma das listas!")
            break

print("\n ***\n")

# imprimindo chaves de um dic
paises_dic = {1: "Angola", 2: "Rwanda", 3: "Congo", 4: "Namibia"}
for chave in paises_dic:
    print(chave)

print()

# imprimindo chave e valor
for chave, valor in paises_dic.items():
    print(chave, valor, end='; ')
