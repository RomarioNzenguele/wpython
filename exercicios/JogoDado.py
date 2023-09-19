import random

'''
     * Fluxo condicional: Jogo de dados
     * 
     * -Qual o palpite?
     * -Qual o valor do Dado?
     * -Palpite esta correto?
'''
# Palpite do User
palpite = int(input("Seu palpite: "))
 
# Lançamento do dado e verificação do palpite
dado = random.randint(1, 6)  # Gera um número entre 1 e 6 inclusive


if (palpite == dado):
    print(f"**Acabou de acertar\n Palpite = {palpite} e Dado = {dado}")
else:
    print(f"**Errado\n Palpite = {palpite} e Dado = {dado}")
