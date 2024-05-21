#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input())
n2 = int(input())
n3 = int(input())

numeros = []

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)

numeros.sort(reverse=True)
print(numeros)