print("""[Exemplo 4] Escreva um programa que para mostrar um cabeçalho + Formatação da impressão""")
nome =input('Qual seu nome? ')
print('='*40)
print('Bem-vindo, {:>10}'.format(nome)) # ALINHAMENTOS {:>10}
print('='*40)
print('Bem-vindo, {:20}'.format(nome))
print('Bem-vindo, {:>20}'.format(nome))
print('Bem-vindo, {:<20}'.format(nome))
print('Bem-vindo {:^20}'.format(nome))
print('Bem-vindo, {:=^20}'.format(nome))
