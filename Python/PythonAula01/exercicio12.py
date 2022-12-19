print('>>>>[exerício 12] Escreva um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.<<<<\n')

print('#'*10, 'REAJUSTE SALARIAL', '#'*10)
salario = float(input('\nDigite seu salário: R$'))

aumento = salario + (salario * 15 / 100)
t_aumento = salario * 0.15

print('\nSeu salário atual é de R${:.2f}\n Com o aumento de 15% passará a receber: R${:.2f} \nVocê recebeu R${:.2f} de aumento! Meus Parabéns! \n'.format(salario,aumento,t_aumento))
print('#'*18, 'FIM', '#'*18)