# Tipos Primitivos + Saida de dados
# ( int = números inteiros 8, 9 ,- 10) (float = números reias ou de ponto flutuante 4.5 - 0.0750)
# ( bool = valores lógicos ou Boleanos VERDADEIRO OU FALSO) ( str = valores caracteres ou strings 'OLÁ, 7.5')

# [Exercício 3] Escreva um programa que leia dois números do usuário e tente mostrar a soma deles.


n1 =int(input('Digite um número: '))
n2 =int(input('Digite outro número: '))
print(type(n1), type(n2)) # type() FUNÇÃO PARA VERIFICAÇÃO DE DADOS
soma = n1+n2
print('A soma entre {} e {} vale {}'.format(n1,n2,soma))