#Faça um Programa que peça dois números e imprima o maior deles.

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(f"{n1} = {n2}")