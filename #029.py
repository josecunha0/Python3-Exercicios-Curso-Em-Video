# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite. 

v = float(input("Qual é a velocidade atual do carro? "))

if v > 80:
    print("-=-"*20)
    print("Você recebeu uma multa por exceder o limite de 80Km/h.")
    multa = (v-80)*7
    print(f"Você terá que pagar uma multa no valor de R${multa:.2f}!")
    
print("-=-"*20)
print("Tenha um bom dia! Dirija com segurança!")
