# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from time import sleep
from datetime import date

print("-=-"*22)
print("O ano bissexto ou não?".upper().center(50))
print("-=-"*22)
sleep(1)

ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
sleep(1)
print("Processando as informações...")
sleep(3)
print("-=-"*22)

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é um ano bissexto.")
    print("-=-"*22)
else:
    print(f"O ano de {ano} não é um ano bissexto.")
    print("-=-"*22)
