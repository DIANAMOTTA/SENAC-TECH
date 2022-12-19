#[Exercício 10] Escreva um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para  pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

print('#'*10, 'DIGITE AQUI AS DIMENÇÕES PARA CALCULAR QUANTOS LITROS DE TINTA IRÁ PRECISAR','#'*8)
l = float(input('Digite a largura (M): '))
a =float(input('Digite a altura: (M): '))
print('*'*85)
area = l * a
print(f'Sua parede têm a dimensão de: {l}x{a}m² e o total de sua área é: {area}m² '.format(area))

calculo = area / 2
print(f'Você precisará de {calculo}Litros de tintas para pintar sua parede! '.format(calculo))
print('*'*40, 'FIM', '*'*40)