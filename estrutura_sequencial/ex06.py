#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

pi = float(3.14)
raio = float(input("Digite o raio do circulo em metros: "))
calc = float(pi * (raio ** 2))
print(f"A área é: {calc}m")