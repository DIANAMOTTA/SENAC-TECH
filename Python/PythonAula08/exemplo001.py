#[Exemplo 1] Escreva um programa que leia vários números inteiros e só pare quando o usuário digitar o valor 999.
#No final, mostre a soma entre eles

mumero = soma = 0
while True:
    numero = int(input('Digite um número [999 to exit]: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale {soma}')

