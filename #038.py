# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

from time import sleep

print("-="*20)
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print("Analisando...")
sleep(2)

print("-="*20)
if num1 > num2:
    print(f"O maior valor é o {num1}!")
elif num2 > num1:
    print(f"O maior valor é o {num2}!")
else:
    print("Os valores são iguais.")
print("-="*20)
