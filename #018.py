'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
'''

from math import radians, sin, cos, tan

an = float(input("Digite o ângulo que você deseja calcular: "))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print(f"O valor do SENO do ângulo {an}, é {seno:.2f}")
print(f"O valor do COSSENO do ângulo {an}, é {cosseno:.2f}")
print(f"O valor do TANGENTE do ângulo {an}, é {tangente:.2f}")
