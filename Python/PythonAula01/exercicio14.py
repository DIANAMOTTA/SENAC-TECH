print('[Exercício15] Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.'
      '\n Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.\n')

print('#'*20,'ALUGUEL DE CARROS', '#'*20)

qkm = float(input('\nQuantos Km rodados? '))
qdias = int(input('Quantos dias alugados? '))

km = qkm * 0.15
dias = qdias * 60
total = dias + km
#pago =(dias * 60) + (km * 0.15)
print('O custo pela locação diaria R${:.2f}\nCusto por Km rodado R${:.2f}\n'.format(dias,km))
print('Total a pagar: R${:.2f}\n'.format(total))
print('#'*25,'FIM', '#'*28)