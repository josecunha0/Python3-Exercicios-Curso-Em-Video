 '''
 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
 '''

d = float(input("Quanto em real você possui? R$"))
conv = d / 4.73
print(f"Com R${d:.2f} na carteira, você consegue comprar ${conv:.2f}!")
