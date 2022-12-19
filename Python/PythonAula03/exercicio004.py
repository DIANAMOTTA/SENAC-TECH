print("""[Exercício 4] Escreva um programa que:
leia o nome completo de uma pessoa e diga se ela tem “Silva” no nome.""")

nome = str(input('Digite seu nome completo: ')).strip()#remove espaços

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))#usa operado in para verificar se a string SILVA está dentro do nome sobrenome

