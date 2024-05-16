#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: A) Para homens: (72.7*h) - 58 B) Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura em metros: "))
peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

print(f"Peso ideal para homens: {peso_ideal_homens}\n")
print(f"Peso ideal para mulheres: {peso_ideal_mulheres}")