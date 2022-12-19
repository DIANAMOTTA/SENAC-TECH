print("""[Exercício 7] Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.""")

salario = float(input('Digite seu salario: '))

aumento = salario + (salario * 15)/100
aumento1 = salario + (salario * 10)/100

if aumento1 > 1.250:
    print('Você teve um aumento de 10% e seu novo salario é de R${}'.format(aumento1))
else:
    print('Você teve um aumento de 15% e seu novo salario é de R${}'.format(aumento))
