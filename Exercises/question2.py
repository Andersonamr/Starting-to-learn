# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Essa é uma calculadora para média das suas notas. Escreva quatro notas.")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

res = (nota1 + nota2 + nota3 + nota4) / 4

print(" A sua média é: {}".format(res))
