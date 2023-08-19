import random

'''
     * Loop + Fluxo condicional: Jogo de dados
     * 
     * -Qual o palpite?
     * -Qual o valor do Dado?
     * -Palpite esta correto?
'''

numero_correto = random.randint(1, 10)
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite: "))

    for _ in range(1):  # Usamos um loop for apenas para fins de estrutura
        if palpite == numero_correto:
            print("Parabéns! Você acertou!")
            break  # Sai do loop for se o palpite estiver correto
        elif palpite < numero_correto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
    else:
        print("Tentativa incorreta. Tente novamente.")

    tentativas += 1

print("Fim do jogo.")
