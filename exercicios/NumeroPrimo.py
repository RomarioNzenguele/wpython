import math

# Verificando se um número é primo


def isPrimo(n):
    if (n % 2) == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i) == 0:
            return False
    return True
