    #Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # Comprar apenas latas de 18 litros;
    # Comprar apenas galões de 3,6 litros;
    # Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima isto é, considere latas cheias.

import math

tamanho_area = float(input("Digite o tamanho da área em m²: "))
quantidade_litros = tamanho_area / 6 * 1.10
print(f"Serão necessários {quantidade_litros:.2f} litros de tinta com 10% de folga.")
quantidade_latas = math.ceil(quantidade_litros / 18)
preco_latas = quantidade_latas * 80.00
print(f"Ao comprar apenas latas de 18 litros, você precisará de {quantidade_latas} latas e pagará R$ {preco_latas:.2f}.")
quantidade_galoes = math.ceil(quantidade_litros / 3.6)
preco_galoes = quantidade_galoes * 25.00
print(f"Ao comprar apenas galões de 3,6 litros, você precisará de {quantidade_galoes} galões e pagará R$ {preco_galoes:.2f}.")
latas_necessarias = quantidade_litros // 18
litros_restantes = quantidade_litros % 18
galoes_necessarios = math.ceil(litros_restantes / 3.6)
preco_misto = (latas_necessarias * 80.00) + (galoes_necessarios * 25.00)
print(f"Para minimizar o desperdício, você precisará de {int(latas_necessarias)} latas e {galoes_necessarios} galões, e pagará R$ {preco_misto:.2f}.")