print("""[Exercício 8] Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.""")
#REGRA PARA FORMAR UM TRIANGULO -->>> CADA UM DOS SEGUIMENTOS TEM QUE SER MENOR DO QUE A SOMA DO COMPRIMENTO DOS OUTROS DOIS


l1 = float(input('Digite um lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

v1 = (l1 < l2 + l3)
v2 = (l2 < l1 + l3)
v3 = (l3 < l1 + l2)
# if l1 < l2 + l3 and r2 < l1 + l3 and l3 < l1 + r2: CADA UM DOS SEGUIMENTOS TEM QUE SER MENOR DO QUE A SOMA DO COMPRIMENTO DOS OUTROS DOIS
if v1 and v2 and v3: # condição para verificar os valores boleanos atribuidos nas condições para v1 v2 v3
    print('GERA UM TRIANGULO')
else:
    print('NÃO GERA UM TRIANGULO')