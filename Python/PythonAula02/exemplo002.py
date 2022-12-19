print('[Exemplo 2]Escreva um programa que leia um número do usuário e mostre a raíz quadrada desse número e arredonde para cima esse número se for necessário.')

# importa biblioteca matematica -> sqrt importa função raiz2
from math import sqrt
num = float(input('Digite um valor para exibir a RaizQ: '))
raiz = sqrt(num)

print('A raizQ de {} é {:.2f}'.format(num,raiz))