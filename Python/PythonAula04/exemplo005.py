print("""[Exemplo 5] Escreva um programa que:
leia duas notas do user e calcule a média.
Se a média for maior que 7, retorne APROVADO.
Caso contrário, retorne REPROVADO.""")

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2)/2
print(media)
if media >= 7:
    print('Aprovado! Sua media foi de {}'.format(media))
else:
    print('Reprovado! Sua nota foi {} e ficou abaixo da média'.format(media))
