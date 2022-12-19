

print("""[Exercício 1] Escreva um programa que o computador pensará em um número entre 0 e 5.
Em seguida, o usuário deverá adivinhar esse valor. Caso o usuário acerte, retorne “VENCEU”, caso perca, retorne “PERDEU”.""")

# importa modulo randon
import random
from time import sleep

jogador = int(input('Vamos jogar o jogo do adinha, Escolha um número entre 0 e 5 e tente adivinhar '))# jogador tenta adivinhar

print('\033[1:34mPROCESSANDO...\033[m')
sleep(1)
# usando a função randint para gerar números aleatórios (0,5)
maquina = random.randint(1,5)
if maquina == jogador:
    print('\033[1:34mParabéns! Voçê venceu! Eu pensei no número {}\033[m'.format(maquina))
else:
    print('\033[1:32mTente novamente, Você perdeu!\033[m')


