# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

from time import sleep

print("-=-"*18)
distancia = float(input("Qual é a distância da sua viagem em Km? "))

print("-=-"*18)
print(f"Você está prestes a começar uma viagem de {distancia}Km")
sleep(1)

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
    
print(f"E o preço da sua passagem será de R${preço:.2f}")
print("-=-"*18)
print("Faça uma excelente viagem!")
