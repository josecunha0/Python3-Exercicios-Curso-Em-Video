# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar ou se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc

print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
print("-="*22)

if idade == 18:
    print("Você tem que se alistar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o alistamento.")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos!")
print("-="*22
