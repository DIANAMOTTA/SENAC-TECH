import a as a

print('[Exemplo 3]Escreva um programa que leia uma string e retorne um “bom dia” ao user, dizendo que o nome dele é bonito caso o nome começar com a letra A.')

nome = str(input('Digite seu nome: ')).strip()
#função upper passa para caixa alta e [0] lê a primeira letra da string verifica se é verdade e executa bloco if
if nome.upper()[0] == 'A': # se o nome digitado for começa com a letra A então condição é verdadeira, executa if
    print('Bom dia! Seu nome comça com a letra A')
else:
    print("Que pena, seu nome não começa com a letra A ")