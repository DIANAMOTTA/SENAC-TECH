#[Exercício 8] Escreva um programa que leia vários números inteiros e só pare quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
contador = soma = 0
num = int(input('Digite um número inteiro ou [999 to exit]: '))
while True:
    if num != 999:
        break

    num = int(input('Digite um número inteiro ou [999 to exit]: '))
    contador += 1
    soma += 1
print(f'A soma é {soma}')
print((f"Você digitou {contador}"))