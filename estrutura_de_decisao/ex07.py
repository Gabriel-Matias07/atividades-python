#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número.")
elif n3 > n1 and n3 > n2:
    print(f"{n3} é o maior número.")

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número.")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor número.")
elif n3 < n1 and n3 < n2:
    print(f"{n3} é o menor número.")