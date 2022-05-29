# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input("Qual o preço do produto? R$"))
desconto = p * (5/100)
total = p - desconto
print(f"O produto que custava R${p:.2f}, agora com o desconto de 5% passa a custar R${total:.2f}!")
