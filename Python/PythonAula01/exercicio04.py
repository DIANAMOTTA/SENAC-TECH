#[Exercício 4] Escreva um programa que leia um número e mostre seu antecessor e seu posterior.

n= int(input('Digite um número inteiro: '))
print('Analisando o valor {}, seu antecessor é: {}, sucessor é: {}'.format(n, (n-1), (n+1)))