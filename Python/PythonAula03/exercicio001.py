print("""[Exercício 1] Escreva um programa que leia o nome completo de uma pessoa e mostre:
1)	O nome com todas as letras maiúsculas;
2)	O nome com todas as letras minúsculas;
3)	Quantas letras ao todo (sem considerar os espaços);
4)	Quantas letras tem o primeiro nome.
""")

nome = str(input('Digite seu nome completo:  ')).strip()
print('Analisando seu nome: ')
print('o nome em letras maiúsculas:  {}'.format(nome.upper()))
print('O nome em letras minusculas {}:  '.format(nome.lower()))
print('Quantidade de letras no primeiro nome:{}'.format(len(nome) - nome.count(' '))) #len identifica o comprimento de uma string >>> count contagem direcionada
print('Seu primeiro nome tem:  {}'.format(nome.find(' ')))#find = busca por trechos na string
separa = nome.split()
print('Seu primeiro nome é {} e têm {}'.format(separa[0], len(separa[0])))

