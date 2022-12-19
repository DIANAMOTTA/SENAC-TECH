print('[Exercício 12] Escreva um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.')


sal = float(input('Digite o salário: '))
aumento = sal+(sal * 0.15)
t_aumento = sal * 0.15
print('Você receberá um aumento de: {:.2f}'.format(t_aumento))