# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_colaborador = float(input("Digite o valor do seu salário: "))
antes_reajuste = salario_colaborador

if salario_colaborador <= 280.00:
    percentual = 20
elif salario_colaborador > 280.00 and salario_colaborador < 700.00:
    percentual = 15
elif salario_colaborador > 700.00 and salario_colaborador < 1500.00:
    percentual = 10
elif salario_colaborador > 1500.00:
    percentual = 5
else:
    print("Entrada inválida!")

salario_colaborador += (percentual/100) * salario_colaborador

print(f"Salário antes do reajuste: R${antes_reajuste:.2f}")
print(f"Percentual aplicado: {percentual}%")
print(f"Valor de aumento: R${(percentual / 100) * antes_reajuste:.2f}")
print(f"Novo salário: R${salario_colaborador:.2f}")