# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: R$"))

a1 = salario * 15/100
a2 = salario * 10/100

if salario <= 1250:
    print(f"Com o aumento de 15%, o novo salário passa a ser R${salario + a1:.2f}")
else:
    print(f"Com o aumento de 10%, o novo salário passa a ser R${salario + a2:.2f}")
