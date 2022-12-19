print("""fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")
print(">>>>>>>FORMAS DE FATIAR UMA STRING")
frase = 'Bom-dia: '
print(frase)
#Os dois valores server para varrer uma string;
print(frase[5]) # mostra o valor de um caracter, número 5 é a posição do caracte que quero 'pegar'
print(frase[1:4]) #mostra o valor de mais de um caracter quero 'pegar'
print(frase[1:2:2]) #Pegando mais de um caracter mas com um salto --> O último valor nos informa o salto que queremos dar
print(frase[:4]) #Não informar o valor inicial, indica ao Python que, por padrão, ele deverá varrer a string do começo, ou seja, do zero,  até o valor anterior ao informado. No nosso caso, de 0 até 3.
print(frase[2:])#Informando o primeiro valor, mas não o último, o Python entenderá como ler essa string partindo do valor informado até o final.
print(frase[1::2])#Varrendo uma string de um ponto até o final com salto:

print(">>>>>>>ANÁLISE - IDENTIFICANDO O COMPRIMENTO DE UMA STRING")
print(len(frase))# identifica o comprimento de uma string
print(frase.count("a", 0, 4))#<string>.count(“<caracter>”, <início>, <fim + 1>) faz uma contagem direcionada
print(frase.find("ia"))#<string>.find(“<pedaço> essa função retorna se ele encontrou ou não o trecho buscado E onde começou esse trecho.”)
print(frase.find("Diana"))#Se essa função retornar “-1”, isso quer dizer que o valor passado para função NÃO EXISTE dentro da string que estamos procurando.
print("Diana" in frase)#Essa função IN retorna True ou False. Apenas no informando se há ou não aquele trecho dentro da string que estamos analisando
print(">>>>>>>FUNÇÕES PARA TRANSFOR - OU SUBSTITUIR UMA STRING")
print(frase.replace("Bom-dia", "Diana"))#<string>.replace(“<antigo>”, “<novo>”)Essa função substitui a sequência de caracteres procurada, pela nova sequência escolhida. Essa realocação altera o tamanho da string.
print(frase)
print(frase.upper())#caixa alta = trasforma a string em Mainusculas
print(frase.lower())#caixa baixa =  trasforma a string em minusculas
print(frase.capitalize())# trasforma a string em minusculas e transforma apenas a primeira entra em maisculo
print(frase.title())#trasforma a string em minusculas e transforma a primeira entra em maisculo em uma frase = Diana Rosa Motta
print(frase.strip())# remove todos os espaços vazios na string
print(frase.rstrip())# remove espaços vazios na string da direita
print(frase.lstrip())# remove espaços vazios na string a esquerda
print(">>>>>>>FUNÇÕES PARA DIVIDIR UMA STRING")
nome = 'Diana Rosa Motta'
print(nome.split())# divide as strings gerando um ou mais indices novos
print(nome.split()[0]) #mostra apenas o primeiro indice
print(nome.split()[1])#mostra apenas o segundo indice
print(nome.split()[2])#mostra apenas o terceiro indice
print(nome.split()[0][2])##mostra apenas o primeiro indice
print(">>>>>>>FUNÇÕES PARA JUNTAR UMA STRING")
nome1 = 'muito obrigado'
print(nome1.split())
print("-".join(nome1.split()))
print(" ".join(nome1.split()))
print("*".join(nome1.split()))