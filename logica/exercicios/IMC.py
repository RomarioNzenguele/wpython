# Exemplo basico do calculo do IMC

peso = float(input("Peso (Kg): "))
altura = float(input("Altura (m): "))

imc = peso / altura**2

print("Peso Ideal") if (imc >= 20 and imc <=
                        25) else print("Fora do peso ideal")
print(f"Imc = {round(imc)}") 