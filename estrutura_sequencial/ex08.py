#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha no mês? "))

calc_mes = float(ganho_por_hora * horas_trabalhadas)
print(f"Você ganha R${calc_mes} por mês!")