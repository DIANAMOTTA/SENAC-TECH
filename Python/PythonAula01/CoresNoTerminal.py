
     #style      #back
#\033[0    :33:   44m
           #text

# CODIGO DO STYLE -> 0 none(NADA)  1 bold(NEGRITO) 4 Underline(SUBLINHA A LETRA) 7 negative(INVERTE)
# CODIGO DE COR TEXT -> 30(BRANCO) 31(VERMELHO) 32(VERDE) 33(AMARELO) 34(AZUL) 35(ROXO) 36(SIANO) 37(CINZA)
# CODIGO BACKGROUG 'cor de fundo' -> 40(BRANCO) 41(VERMELHO) 42(VERDE) 43(AMARELO) 44(AZUL) 45(ROXO) 46(SIANO) 47(CINZA)

# \033[0:30:41m
# \033[4:33:44m
# \033[1:35:43m
# \033[30:42m
# \033[m
# \033[7:30m
print('\033[32m=-='*20)
print('\033[1:31:43mCores no Terminal!\033[m')
print('\033[1:4:30:41mCores no Terminal!\033[m')
print('\033[1:30:45mTESTE CORES\033[m')
print('\033[0:31:40mTESTE\033[m')
print('\033[31m=-='*20)
a = 3
b = 5
nome = 'Diana'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretopebranco'],nome))
print('\033[mOs valores são \033[32m{} \033[me \033[31m{}'.format(a,b))
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[m',nome,'\033[m'))