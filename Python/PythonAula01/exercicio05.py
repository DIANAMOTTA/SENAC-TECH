# [Exercício 5] Escreva um programa que leia um número e mostre o dobro, o triplo e raíz quadrada.

num = int(input('Digite um número: '))
#dobro = num * 2
#triplo = num * 3
#raiz = num**(1/2)
#print('O dobro de', num, f'é: {dobro} \nO triplo de', num, f'é: {triplo} \nA raiz de', num, 'é: {}'.format(dobro,triplo,raiz))
print('O dobro de {} vale: {}'.format(num,(num*2)))
print('O tripo de {} vale: {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(num, (num*3),num,(num**(1/2))))