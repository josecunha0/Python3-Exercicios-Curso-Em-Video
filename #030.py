# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep

print("-=-"*10)
n = int(input("Digite um número: "))

resultado = n % 2
print("Processando...")
sleep(1.5)

if resultado == 0:
    print("-=-"*10)
    print(f"O número {n} é PAR.")
    print("-=-"*10)
else:
    print("-=-"*10)
    print(f"O número {n} é ÍMPAR.")
    print("-=-"*10)
