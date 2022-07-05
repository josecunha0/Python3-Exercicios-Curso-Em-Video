------------------------------------------------------------------------------
# Primeira lista #
------------------------------------------------------------------------------
#Atividade 1: 
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
quinze = idade + 15
print(f"Olá, {nome}! \nDaqui 15 anos, você terá {quinze}.")
------------------------------------------------------------------------------
#Atividade 2: 
dol = float(input("Quantos dólares você quer comprar? $"))
cotacao = dol * 5.33
print(f"Para comprar ${dol:.2f}, você precisa de R${cotacao:.2f}")
------------------------------------------------------------------------------
#Atividade 3:
salario = float(input("Digite o valor do seu salário: R$"))
dias = int(input("Quantos sábados trabalhou nesse mês? "))

if dias <= 4 and dias >= 1:
    soma = (dias * 200) +  salario
    print(f"O total a receber é: R${soma:.2f}")
elif dias == 0:
    print(f"O total a receber é: R${salario}")
else:
    print("Erro! \nAs entradas possíveis vão de 0 até 4.")
--------------------------------------------------------------------------------
#Atividade 4:
C = float(input("Digite a temperatura em Celsius: "))
conv = (C * 1.8) + 32
print(f"A temperatura {C:.1f}°C convertida para Fahrenheit fica {conv:.1f}°F")
--------------------------------------------------------------------------------
#Atividade 5: 
n = int(input("Digite um valor: "))

if n == 0:
    print("O valor informado é igua a zero.")
elif n < 0:
    print("O valor informado é menor do que zero.")
else: 
    print("O valror informado é maior do que zero.")
--------------------------------------------------------------------------------
# Segunda lista #
--------------------------------------------------------------------------------
#Aividade 1: 
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if x > y:
    print(f"O valor x({x}) é maior que y({y}).")
elif y > x:
    print(f"O valor y({y}) é maior que x({x}).")
else: 
    print("Os valores informados são iguais.")
---------------------------------------------------------------------------------
#Atividade 2:
sanduiche = float(input("Digite o valor do sanduiche: R$"))
print ("-="*20)
print("Terá adicional? ")
add = int(input("1-SIM/2-NÃO \nR:"))

if add == 1:
    soma = sanduiche + 8
    print ("-="*20)
    print(f"O valor total será R${soma}")
elif add == 2:
    print ("-="*20)
    print(f"O valor total será R${sanduiche}")
else:
    print ("-="*20)
    print("Resposta inválida!! \nApenas 1 ou 2.")
---------------------------------------------------------------------------------
#Atividade 3:
produto = float(input("Digite o valor do produto: R$"))
forma = int(input("Qual a forma de pagamento? \n1-À vista   2-Parcelado \nR:"))

if forma == 1:
    desconto = produto - (produto * (5/100))
    print(f"Pagando à vista você ganhou 5% de desconto, preço final: R${desconto:.2f}")
elif forma == 2:
    parcelas = int(input("Qual será a quantidade de parcelas? (1 a 10) \nR:"))
    parcelado = produto / parcelas
    print(f"O produto ficará em {parcelas}x de {parcelado}")
else:
    print("Opção inválida!! \nApenas 1 ou 2.")
---------------------------------------------------------------------------------
#Atividade 4: 
salario = float(input("Digite o seu salário: "))

if salario <= 2000.00:
    soma = salario + 300
    print(f"Seu novo salário será de: {soma:.2f}")
else:
    soma = salario + 400
    print(f"Seu novo salário será de: {soma:.2f}")
---------------------------------------------------------------------------------
#Atividade 5: 
idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Você ainda não tem idade para votar.")
elif idade >= 16 and idade < 18:
    print("O voto par você é facultativo, você pode votar mas não é obrigatório.")
elif idade >= 18 and idade < 70:
    print("O voto para você é obrigatório, verifique sua situação em um Cartório Eleitoral.")
else:
    print("O voto para a sua idade é facultativo.")
