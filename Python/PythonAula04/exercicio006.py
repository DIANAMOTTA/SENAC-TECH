print("""[Exercício 6]Escreva um programa que leia três números e mostre qual é o maior e qual é o menor.""")

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
#verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
   menor = n2
if n3 < n1 and n3 < n2:
   menor = n3
#verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))