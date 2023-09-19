# Declaracao
a = """Python is good language.
For many professionals, is the best language to start."""
print(a)

# Indexacao [Slicing]
a = "Romario Nzenguele!"

print(a[1])  # imprimindo o segundo caracter da string -> o
print(a[7])  # imprime o oitavo caracter -> espaco
print(a[2:5])  # imprime do terceiro ate ao quinto caracter -> mar
print(a[:5])  # imprime do primeiro ate ao quinto caracter -> Romar
print(a[2:])  # imprime do terceiro caracter ate ao ultimo -> mario Nzenguele!
print(a[:-3])  # imprime sem os tres ultimos caracteres -> Romario Nzengue
print(a[-4:])  # imprime sem os ultimos quatro caracteres  -> ele!
print(a[-4:-3])  # dos quatro ultimos caracteres, elimina os tres ultimos -> e
print(a[::-1])  # imprimindo de forma reversa

# Modificando strings
a = " Da Silva "
print(a.upper())
print(a.lower())
print(a.strip())  # REMOVER espacos em brancos, semelhante ao trim() em java
print(a.replace("a", "O"))  # SUBSTITUIR 'a' por 'O'

a = "Pyton,Java,C#,JavaScript"
print(a.split(","))  # RETORNA uma lista de acordo com o caracter especificado


# Formatacao
qtd = 3
pu = 300
msg = 'Kit = quantidade x pu = {} x {} = {} AKz'.format(qtd, pu, pu*qtd)
print(msg)
msg = f"Kit = quantidade x pu = {qtd} x {pu} = {pu*qtd} AKz"
print(msg)
