print("""[Exercício 6]Escreva um programa que:
leia  o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente.""")

nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()#slipt divide a string em indices
print('Seu primeiro nome: {}'.format(nome1[0]))#mostra o nome na posição 0
print('Seu ultimo nome: {}'.format(nome1[len(nome1)-1]))#len verifica quantas posições tem o nome



