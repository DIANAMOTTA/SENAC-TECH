print("""[Exercício 2] Escreva um programa que leia um número entre
 0 e 9999 e mostre cada um dos dígitos separados mostrando quantas unidades,
dezenas, centenas e milhares há nesse número. """)


num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade = {} '.format(u))
print('Dezena = {}'.format(d))
print('Centezas = {} '.format(c))
print('Milhar = {} '.format(m))
