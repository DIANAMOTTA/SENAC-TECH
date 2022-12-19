#[Exercício 9] Escreva um programa que leia o valor que tu tens em reais e converta para dólares.

print('*'*12, 'CONVERSOR DE MOEDAS', '*'*12)
reais = float(input('\nDigite o valor em (RS:) : '))
cot = reais/5.33
print('\nCom R${:.2f} você pode comprar US${:.2f}\n'.format(reais, cot))
print('*'*18, 'FIM', '*'*18)
