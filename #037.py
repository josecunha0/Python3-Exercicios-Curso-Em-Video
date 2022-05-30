# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um número inteiro: "))
print("-="*20)

print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL'''.center(50))
print("-="*20)

opcao = int(input("Sua opção: "))
print("-="*20)

if opcao == 1:
  print(f"{num} convertido para binário, é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para octal, é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal, é igual a {hex(num)[2:]}")
else:
    print("Digite uma opção válida.")
print("-="*20)
