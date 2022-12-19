#[Exercício 9] Escreva um programa que leia vários números.
# No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lido.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
media = soma = quantidade = maior =  menor = 0
while resp in 'Ss':
    num = int(input('Digite um número [999 to exit]: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > menor:
            maior = num
        if num < maior:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a mé dia foi {media}')
print(f'O maior número foi {maior} e o menor número foi {menor}')