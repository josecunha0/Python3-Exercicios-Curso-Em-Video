# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint 
from time import sleep

pc = randint(0, 5) #faz o computador pensar
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5, tente adivinhá-lo.")
print("-=-"*20)

jog = int(input("Em que número eu pensei? ")) #Jogador tenta adivinhar
print("Processando...")
sleep(3)

if jog == pc:
    print("-=-"*20)
    print(f"Parabéns!! Você acertou em cheio o número {pc}.")
    print("-=-"*20)
else:
    print("-=-"*20)
    print(f"Hummm... Não foi dessa vez. Eu pensei o número {pc}.")
    print("-=-"*20)
