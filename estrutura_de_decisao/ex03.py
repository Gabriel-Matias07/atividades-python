#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra_digitada = input("Digite F ou M: ").upper()

if letra_digitada == 'F':
    print("F - Feminino")
elif letra_digitada == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido")