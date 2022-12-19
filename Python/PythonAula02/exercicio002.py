print('[Exercício 2] Escreva um programa que leia os dois catetos de um triângulo retângulo e retorne o comprimento da hipotenusa.')

import  math
co =float(input('Cumprimento do Cateto Oposto : '))
ca = float(input('Cumprimento do Cateto Adjancente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)

print(hi)

