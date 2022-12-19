print('[Exercício 4]Escreva um programa que leia  o nome de quatro alunos e sorteie aleatóriamente um deles,  mostrando o nome na tela.')

import random

nome = str(input('1º aluno: '))
nome1 = str(input('2º aluno: '))
nome2 = str(input('3º aluno: '))
nome3 = str(input('4º aluno: '))

lista = [nome, nome1, nome2, nome3]
escolha = random.choices(lista) # retorna vários elementos aleatórios da lista com substituição.

print(f'A pessoa escolhida foi {escolha}')


