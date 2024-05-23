# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Digite as 4 notas bimestrais: ")
notas = []
soma = 0
for i in range(4):
    valor = float(input(f"Digite a nota {i + 1}: "))
    notas.append(valor)
for nota in notas:
    soma = soma + nota
resultado = soma / len(notas)
print(f"Resultado = {resultado}")