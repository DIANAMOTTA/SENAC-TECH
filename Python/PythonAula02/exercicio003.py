print('[Exercício 3] Escreva um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')

from math import radians, sin, cos, tan
num =int(input('Digite o ângulo: '))
seno = sin(radians(num)) # converter para radianos para ler o valor do seno, cosseno e tangente
cos = cos(radians(num))
tan = tan(radians(num))
print('Seno {:.2f} Cosseno {:.2f} e Tangente {:.2f}'.format(seno, cos, tan))