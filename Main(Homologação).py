import random
from Import import  lives_visual_dict
from palavras import palavras

print('-=' * 20)
print(' ' * 10, 'JOGO DA FORCA')
print('-=' * 20)


#Também poderíamos fazer usando funções o que acha?
#Tentei fazer por meio do palavras.txt, mas sem sucesso.
#Podemos fazer este algoritmo por uma função se achar melhor, assim, só precisaremos chamá-la

def palavras_aleatorias(palavras):
    wrd = random.choice(palavras)
    while '-' in wrd or ' ' in wrd:
        wrd = random.choice(palavras)

    return wrd.upper()


#E fazer o JOGO DA FORCA ser uma função também, o que acha?
def forca():
    print(palavras_aleatorias(palavras))

#Consegui essas 3 formas de fazer:

# 1 - De manei mais rápida, achei dessa forma:
wrd = random.choice(palavras) #wrd = word
print(wrd.upper())

#2 - Usando o "palavras_aleatórios" como função dentro da função "Forca".
forca()

#3 - Usar apenas a função "palavras_aleatorias" e ficar chamando ela.
print(palavras_aleatorias(palavras))
