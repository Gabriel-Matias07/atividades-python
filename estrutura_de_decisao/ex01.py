#Faça um Programa que peça dois números e imprima o maior deles.

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

if n1 > n2:
    print(f"{n1} > {n2}")
elif n2 > n1:
    print(f"{n2} > {n1}")
else:
    print(f"{n1} = {n2}")