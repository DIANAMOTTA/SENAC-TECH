#[Exercício 6] Escreva um programa que leia o nome de um aluno, duas notas dele e mostre a média dessas notas.

nome = input('Digite seu nome: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média do aluno é: {}'.format(media))