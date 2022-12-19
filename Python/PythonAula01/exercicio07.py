#[Exercício 7] Escreva um programa que leia um valor em centímetros e mostre em milímetros.

print('='*10, 'Conversão de Medidas', '='*10)
medida = float(input('Informe o valor em (CM): '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))