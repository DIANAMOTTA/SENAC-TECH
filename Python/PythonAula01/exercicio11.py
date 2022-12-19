print('[Exercício 11] Escreva um programa que leia o valor de um produto e mostre ele com 5% de desconto.\n')

print('*'*15,'DESCONTO', '*'*15)
preço = float(input('\nQual valor do Produto? R$: '))
novo = preço - (preço * 5 / 100)

print('\nO produto que custava R${} \nNa promoção com desconto de 5% custará: R${}'.format(preço,novo))
print('\n')
print('*'*19, 'FIM', '*'*19)