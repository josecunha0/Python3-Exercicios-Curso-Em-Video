'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa.
'''

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"O valor da hipotenusa é {hi:.1f}")
