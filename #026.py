# Faça um programa que leia uma frase pelo teclado e mostre: 
# - Quantas vezes aparece a letra "a".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

texto = str(input("Digite seu texto: ")).upper().strip()

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Analisando seu texto...")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("A letra 'A' aparece {} vezes no texto.".format(texto.count('A')))
print("A primeira letra 'A' aparece na posição {}".format(texto.find('A')+1))
print("A última letra 'A' aparece na posição {}".format(texto.rfind('A')+1))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
