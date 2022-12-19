print('[Exercício 14] Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.\n')

print('*'*10,'CONVERSOR DE TEMPERATURAS', '*'*10)
C = float(input('\nInforme a temperatura em ºC: '))

F = C * 1.8+32 #((9*C)/5) +32
print('A temperatura de {}ºC corresponde a {}F'.format(C, F))
