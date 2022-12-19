# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

algo = input('Digite algo que te mostro o tipo primitivo e algumas informações sobre ele:\n ' )
print('Tipo primitivo é:', type(algo))
print("Só têm espeço ?",algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabetica? ', algo.isalpha())
print('É alfanuméricos? ', algo.isalnum())
print('É caractere ASCII? ', algo.isascii())
print('Só têm maiúsculas? ', algo.isupper())
print('Todas as letras são minúsculas? ', algo.islower())
print('É decimal? ', algo.isdecimal())