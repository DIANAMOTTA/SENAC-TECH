print('[Exercício 1] Escreva um programa que leia um número real qualquer e mostre a sua porção inteira.')

import math
num =float(input('Digite um valor real: '))

inteiro = math.trunc(num) #função para mostrar a parte inteira

print('O valor digitado foi {} e sua porção ineira é {}'.format(num,inteiro))
