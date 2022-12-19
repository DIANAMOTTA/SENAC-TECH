import random

print('[Exercício 5]Escreva um prorgama que leia o nome de 4 alunos e coloque eles em uma ordem aleatória, monstrando essa ordem na tela.')

import random
n1 = str(input('1º nome: '))
n2 = str(input('2º nome: '))
n3 = str(input('3º nome: '))
n4 = str(input('4º nome: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista) #utilizada para exibir o resultado de uma lista ou de uma tupla de forma embaralhada

print(f'A ordem foi: {lista}')
