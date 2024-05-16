#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: A) O produto do dobro do primeiro com metade do segundo. B) A soma do triplo do primeiro com o terceiro. C) O terceiro elevado ao cubo.

numUm = int(input("Digite o primeiro número inteiro: "))
numDois = int(input("Digite o segundo número inteiro: "))
numTres = float(input("Digite o terceiro número real: "))

calcA = (numUm * 2) * (numDois / 2)
print(f"A) O produto do dobro do primeiro com metade do segundo: {calcA}.")

calcB = (numUm * 3) + (numTres)
print(f"B) A soma do triplo do primeiro com o terceiro: {calcB}.")

calcC = (numTres ** 3)
print(f"C)O terceiro elevado ao cubo: {calcC}.")