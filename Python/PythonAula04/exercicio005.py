print("""[Exercício 5] Escreva um programa que leia um ano qualquer e mostre se ele é BISSEXTO.""")

#importa modulo data atual
from datetime import date
ano = int(input('Digite o ano: Ou coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year #mostra o ano atual no computador

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é bissexto {}'.format(ano))
else:
    print('Não é bissexto! {}'.format(ano))



