#[Exercício 8] Escreva um programa que leia um número e mostre a sua tabuada.

print('_'*12,'TABUADA','_'*12)
num = int(input('Digite um número para saber a tabuada: '))
tab = num * num
print('{}x{} = {:2}'.format(num, 1, num*1))
print('{}x{} = {:2}'.format(num, 2, num*2))
print('{}x{} = {:2}'.format(num, 3, num*3))
print('{}x{} = {:2}'.format(num, 4, num*4))
print('{}x{} = {:2}'.format(num, 5, num*5))
print('{}x{} = {:2}'.format(num, 6, num*6))
print('{}x{} = {:2}'.format(num, 7, num*7))
print('{}x{} = {:2}'.format(num, 8, num*8))
print('{}x{} = {:2}'.format(num, 9, num*9))
print('{}x{} = {}'.format(num,10,num*10))
print('_'*12,'FIM', '_'*12)