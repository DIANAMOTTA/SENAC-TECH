print("""[Exercício 4] Escreva um programa que:
pergunte a distância de uma viagem em Km.
Calcule e peça o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.""")
# preço R$ 0,50 km até 200km
# praço acima de 200 R$ 0,45


distancia = float(input('Informe a distancia da viagem em: [Km] '))
if distancia <= 200: # verifica se a distancia é menor ou igual que 200
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem será de R${}'.format(preço))# print fora da condição mostra o resultado depois que o if else verifica a condição de verdadeiro ou falso






