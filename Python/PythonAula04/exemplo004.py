print("""[Exemplo 4] Escreva um programa que leia:
uma string e retorne um bom dia ao user, dizendo que o nome dele é bonito se começar com a letra A, por exemplo. Caso contrário, apenas diga que o nome é normal.""")

nome = str(input('Digite seu nome: ')).strip()#remove os espaços

#upper passa para caixa alta e [0] lê a primeira letra da string
if nome.upper()[0] == 'D':
    print('Seu nome é muito bonito, verifiquei aqui que ele começa com a letra D')
else:
    print('Humm.. verifiquei que seu nome é bem normal.. que pena :(')
print('Bom dia, {}'.format(nome))
