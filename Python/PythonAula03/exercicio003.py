print("""[Exercício 3] Escreva um programa que:
leia o nome de uma cidade e informe se ela começa com a palavra “Santo”.""")

cidade = str(input('Digite o nome de uma cidade: ')).strip()#remove espaços


print(cidade[:5].upper() == 'SANTO') # :5 verifica a primeira string - upper transforma em maiusculo

