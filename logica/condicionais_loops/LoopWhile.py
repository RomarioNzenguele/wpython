# LOOP While

# imprimindo o intervalo [1;10]
i = 1
while i <= 10:
    print(i)
    i += 1


# imprimindo o download de um ficheiro
i = 0
while i <= 100:
    print(f'Download em {i} %')
    i += 10
else:
    print('Download Concluido Com Sucesso!')

# Usando o pass, break e continue
'''
pass: É um espaço reservado vazio para manter a sintaxe correta.
break: Interrompe completamente o loop atual.
continue: Pula para a próxima iteração no loop, ignorando o restante do código dentro dessa iteração.
'''
print('\n')
for i in range(5):
    if i == 2:
        pass  # Nada acontece aqui, apenas um espaço reservado vazio
    print(i, end=' ')
print()
for i in range(5):
    if i == 2:
        break  # O loop é interrompido quando i é igual a 2
    print(i, end=' ')
print()
for i in range(5):
    if i == 2:
        continue  # A iteração é pulada quando i é igual a 2
    print(i, end=' ')
