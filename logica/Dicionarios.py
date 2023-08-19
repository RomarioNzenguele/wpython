# Nota: Collections em Python possuem tipagem dinamica

# Dicionario
# chave + valor = indexacao (o indice comeca sempre em 0)
# chave e valor podem ser iguais, mas representam coisas diferentes.

paises_dic = {}  # criando um dic vazio
paises_dic = {1: "Angola", 2: "Rwanda", 3: "Congo", 4: "Namibia"}
print("Tamanho:", len(paises_dic), ", tipo: ", type(paises_dic))

# Acessando o valor da segunda chave
print(paises_dic[2])

# Imprimindo os valores e as chaves
print(paises_dic.keys())
print(paises_dic.values())
print(paises_dic.items())  # exibe os dois

# limpando o dic
paises_dic.clear()  # ou: del paises_dic
print(paises_dic)

# ------------------------------
estudantes_dic = {"00A1": "Silva", "00A2": "Ruth", "00A3": "Capitao"}
print("\n\nEstudantes:", estudantes_dic)

# eliminando um item
del estudantes_dic["00A3"]
print("\n\t'Capitao' excluido pela chave: ", estudantes_dic)


# adicionando um item
estudantes_dic["00A3"] = "Capitao"
print("\n\t'Capitao' adicionado novamente: ", estudantes_dic)
# update add mais do que um item
estudantes_dic.update({"00A4": "Francine", "00A7": "Niclette", 20: 20})
print("\n\tEstudantes actualizados:", estudantes_dic)

# Dicionário de listas
produto_dic = {'Valor': 2_000_00, 'Ano': [
    2018, 2017, 2016], 'Cor': ['Azul', 'verde', 'laranja']}
print('\n\nProduto: ', produto_dic)

# acessando valores
print('\n\tBuscando uma cor: ', produto_dic['Cor'][2].capitalize())

produto_dic['Ano'][0] -= 2
print('\n\t Actualizando o ano 2018 para 2016: ', produto_dic)


# Dicionarios aninhados
dict_aninhado = {2023: {'Abril': {28: 'Certificacao XXXX'}},
                 2022: {'Novembro': {20: 'Curso de XXXX'}}}

print("\n\nCurso: ", dict_aninhado[2022]['Novembro'][20])
