'''
Faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

num = int(input("Digite um número: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Analisando o número {num}...")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"A unidade é: [{u}].")
print(f"A dezena é:  [{d}].")
print(f"A centena é: [{c}].")
print(f"O milhar é:  [{m}].")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
