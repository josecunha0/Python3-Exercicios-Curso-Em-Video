# Faça um algotitmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input("Qual é o salário do funcionário? R$"))
a = s + (s * 15/100)
print(f"O salário que antes era R${s:.2f}, com 15% de aumento vai passar a ser R${a:.2f}!")
