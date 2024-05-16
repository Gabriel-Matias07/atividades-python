#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_maximo = 50
excesso = 0
valor_multa = 4.00

peso_peixe = float(input("Digite o peso do seu peixe em kg: "))
print("\n")

if peso_maximo < peso_peixe:
    excesso = peso_peixe - peso_maximo

    calc = excesso * valor_multa

    print("-------Dados do Programa-------\n")
    print(f"Peso do Peixe: {peso_peixe}kg.\n")
    print(f"Excesso: {excesso}kg.\n")
    print(f"Valor da multa pagar: R$ {calc}.\n")
else:
    print("-------Dados do Programa-------\n")
    print(f"Peso do Peixe: {peso_peixe}kg.\n")
    print("Sem excesso. Não há multa a pagar.\n")