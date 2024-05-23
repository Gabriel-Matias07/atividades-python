#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
preco_lata = 80.00
tamanho_area = float(input("Digite o tamanho da área a ser pintada em m²: "))
litros_necessários = tamanho_area / 3
quantidade_latas = math.ceil(tamanho_area / 18)
preco_total = quantidade_latas * preco_lata
print(f"Serão necessárias {quantidade_latas} latas de tinta.\n")
print(f"O preço total é de R$ {preco_total:.2f}")