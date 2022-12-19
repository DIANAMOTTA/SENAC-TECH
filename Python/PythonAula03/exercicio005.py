print("""[Exercício 5] Escreva um programa que leia um frase e mostre:
1)	Quantas vezes aparece a letra “A”;
2)	Em que posição ela aparece pela primeira vez;
3)	Em que posição aparece pela última vez.
""")

nome = str(input('Digite uma frase: ')).strip().upper()
print('A letra a digitada aparece {} vezes'.format(nome.upper().count('A')))#count vai contar a string >A<
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))#busca direcionada em toda string
print('A ultima letra A apareceu na posição {}'.format(nome.rfind('A')+1))#busca direcionada varrendo a string da direita para a esquerda
