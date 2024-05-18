#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra_digitada = input("Digite uma letra: ").upper()

vogais = ['A', 'E', 'I', 'O', 'U']

if letra_digitada in vogais:
    print("Vogal")
else:
    print("Consoante")