print("""[Exercício 3]Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.""")

num = int(input('Digite um número inteiro: '))

#condição para verificar se é vedadeiro ou falso.
if num % 2 == 0: # se o resto da divisão for igual a 0 a condição é verdadeira e então é par
    print('Par')
else:
    print('Impar')
