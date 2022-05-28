 '''
 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
 '''

km = float(input("Quantos Km você percorreu? "))
dias = int(input("Por quantos dias alugou o carro? "))
c1 = km * 0.15
c2 = dias * 60
total = c1 + c2
print(f"Tendo alugado por {dias} dias e percorrido {km:.1f}Km, o total a pagar é de R${total:.2f}!")
