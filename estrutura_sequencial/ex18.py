#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tempo = 60 #Const

tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_link = float(input("Digite a velocidade da sua internet (em Mbps): "))

tempo_download = (tamanho_arquivo * 8) / velocidade_link
tempo_download_minutos = tempo_download / 60 #Tempo de download em minutos
print(f"Levará aproximadamente {tempo_download_minutos:.2f} minutos para o seu arquivo de {tamanho_arquivo}MB ser baixado com velocidade de internet de {velocidade_link}Mbps.")