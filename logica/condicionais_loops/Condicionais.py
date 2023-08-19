# Condicionais

nota = int(input('\nNota:'))

if nota >= 10:
    print("Apto")
else:
    print("N/Apto")
    if nota >= 8:
        print("Mas pode fazer recurso")
    else:
        print("Reprovado")

# Operador elif
idade = int(input('\nIdade:'))

if idade >= 18:
    print("Pode Assistir!")
elif idade > 16:
    print("Pode aguardar pelo proximo filme!")
else:
    print("Nao pode entrar no cinema!")
