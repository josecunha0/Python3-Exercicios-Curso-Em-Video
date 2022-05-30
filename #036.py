# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anos = int(input("Em quantos anos pretende pagar? "))

p = casa / (anos * 12)
min = salario * 30 / 100

print("-="*20)
print(f"Para pagar uma casa que custa R${casa:.2f} em {anos} anos, as prestações serão de R${p:.2f} sem juros.")
print("-="*20)
sleep(2)

if p <= min:
  print("Empréstimo pode ser concedido!")
else: 
  print("O valor da prestação, ultrapassa 30% do seu salário. \nEmpréstimo negado...")
