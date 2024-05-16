#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: A) Salário bruto. B) Quanto pagou ao INSS. C) Quanto pagou ao sindicato. D) O salário líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:

#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#- Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input("Quanto você ganha por hora trabalhada? "))
horas_tabalhadas_mes = float(input("Quantas horas você trabalha por mês? "))

salario_bruto = (ganho_hora * horas_tabalhadas_mes)
imposto_renda = (11/100 * salario_bruto)
inss = (8/100 * salario_bruto)
sindicato = (5/100 * salario_bruto)
descontos = (imposto_renda + inss + sindicato)
salario_liquido = (salario_bruto - descontos)

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Quanto pagou ao INSS: R$ {inss:.2f}")
print(f"Quanto pagou ao sindicato: R$ {sindicato:.2f}")
print(f"Salário Liquido: R$ {salario_liquido:.2f}")