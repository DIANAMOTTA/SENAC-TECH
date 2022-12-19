print("""[Exercício 2]Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.""")


velocidade = float(input('Informe sua velociade em: ( Km ) '))
multa = (velocidade - 80)*7 # ordem de precedencia, primeiro resolve o que está dentro dos parenteses e depois o que está fora
if velocidade > 80:
    print('\033[1:33mVocê foi multado por exesso de velocidade. Sua multa é:  {}\033[m'.format(multa))
else:
    print('\033[1:34mParabéns, você é um bom motorista, está no limite de velociada.\033[m ')
