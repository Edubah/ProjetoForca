'''ALGORITMO EDUARDO'''
import random
from palavras import palavras
'''
print('-=' * 20)
print(' ' * 10, 'JOGO DA FORCA')
print('-=' * 20)
print()

wrd = random.choice(palavras)                                                                        #wrd = word
print(wrd.upper())
'''

''' ALGORITMO MATHEUS '''

'''letras = list(wrd)                                      #Aqui o algoritmo estara jogando cada letra da palavra selecionada de "wrd" em uma lista.
print(letras)

letras_ordem1 = letras[:]
letra_usuario = ()
fim = 6'''

'''while fim > 0:
    letra_usuario = input('Digite uma letra ')
    if letra_usuario in wrd:
        letras_ordem1.append(letra_usuario)
    else:
        fim -= 1
        print(f'Voce errou, restam {fim} chances')
print('Game Over')'''
'''
letra_usu = input('Letra: ')
listateste1 = ['m', 'a', 's', 't', 'o', 'd', 'o', 'n', 't', 'e']
listateste2 = listateste1[:]
tracosteste = []
traco = (' ')
repeticao = listateste2.count(letra_usu)
print(repeticao)
contador = 0
'''
'''
while contador < len(listateste2):
   tracosteste.append(list(traco))
   contador += 1

for i,v in enumerate(listateste2):
    i = tracosteste[i]
    if letra_usu in listateste2:
       tracosteste[listateste2.index(letra_usu)] = letra_usu
    elif repeticao > 1:
'''



'''
letra_usuario = input('Letra: ')
palavra1 = ['b', 'a', 't', 'a', 't', 'a']
palavra2 = palavra1[:]
lacunas = []
for l in palavra2:
    lacunas.append(' ')

contagem = palavra2.count(letra_usuario)  # quantas vezes a palavra se repete na lista
indexinput = palavra2.index(
    letra_usuario)  # retorna o indice da letra que o usuario inputar se a mesma estiver na lista(palavra1)

for i, v in enumerate(palavra2):  # itera sobre todos os indices e valores de (palavra2)
    i = lacunas[i]  # atribui a i o mesmo valor que esta iterando sobre o indice da lista(lacunas)
    lacunas[palavra2.index(
        letra_usuario)] = letra_usuario  # substitui a lacuna vazia pela posicao correta da letra na palavra
    if contagem > 1:  # bloco if caso a letra se repita
        lacunas[palavra2.index(letra_usuario,
                               indexinput + 1)] = letra_usuario  # substitui a lacuna pela letra repetida na posicao correta

print(lacunas)
'''


#letra_usuario = input('Letra: ')
batata = ['a', 'l', 'c', 'a', 'c', 'h', 'o', 'f', 'r', 'a'] #lista
batataC = batata[:]
#count = batata.count(letra_usuario) #contagem de quantas vezes a letra 'a' aparece na lista
lacunas = []
for l in batata:
    lacunas.append('_')



def validacao():
    letra_usuario = input('Letra: ')
    count = batataC.count(letra_usuario)
    for i,v in enumerate(batataC):
        batataC.index(letra_usuario, batataC.index(letra_usuario))
        lacunas[batataC.index(letra_usuario)] = letra_usuario
        i = lacunas[i]
        if count > 1:
            try:
                for i in range(count+1):
                    lacunas[batataC.index(letra_usuario, i+1)] = letra_usuario
            except ValueError:
                pass
    print(lacunas[0:])
print(batataC)

fim = 6
while fim > 0:
    validacao()
    #if validacao() not in lacunas:
      #  fim -= 1
       # print(f'Voce errou, restam {fim} chances')












































