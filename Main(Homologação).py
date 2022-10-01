#Jogo da Forca - Project by Eduardo Santos & Matheus Santos
#ver 1.1 / rev 0.4
#----------------------------------------------------------
import random
from Import import lives_visual_dict as bonequinho
import string
import requests
from requests import sessions


print('-=' * 20)
print(' ' * 10, 'JOGO DA FORCA')
print('-=' * 20)
print()

#url = 'http://papalavras-server.herokuapp.com/words/random/'

with requests.get('http://papalavras-server.herokuapp.com/words/random/') as url:
    def palavra_valida():
        req = url
        word = req.json()
        palavra = word['word']
        return palavra.upper()

def jogo():                                                                                                             # Chamando a função PALAVRA_VALIDA
    wrd = palavra_valida()
    wrd_letras = set(wrd)                                                                                               # Criando a variável para usar o set para evitar palavras duplicadas
    alfabeto = set(string.ascii_uppercase)                                                                              # Variável para atribuir as letras da palavra escolhida como capslock
    letras_usadas = set()                                                                                               # Variável para as letras usadas, quero mostrar quais eles já digitou
    vidas = 7                                                                                                           #Quantidade de vidas, assim já puxo daqui qual das imagens da lista do outro arquivo
    print(wrd)
    while len(wrd_letras) > 0 and vidas > 0:                                                                            # Condição óbvia kkkkk


        print('Você tem', vidas, 'vidas sobrando e você já utilizou estas letras: ', ' '.join(letras_usadas))            # Usei o join para ele não separar as letras por ' '. Ficará assim: # ' '.join(['a', 'b', 'cd']) --> 'a b cd'


        lista_palavras = [letra if letra in letras_usadas else '-' for letra in palavra_valida()]                                    # Aqui criei uma variável e fiz uma pequena função. Uma lista de letras para as letras já usadas
        print(bonequinho[vidas])                                                                                        # Aqui mostrará a parte do boneco baseado na quantidade de vidas!
        print('Palavra atual: ', ' '.join(lista_palavras))                                                              #   Mesmo princípio do primeiro JOIN

        letra_usuario = input('Adivinhe a letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:                                                                   # Usei a subtração para verificar se a letra inserida não está entre as duas variáveis
            letras_usadas.add(letra_usuario)                                                                            # A letra inserida vai para as letras usadas
            if letra_usuario in wrd_letras:                                                                             # Se a letra estiver dentro da palavra selecionada
                wrd_letras.remove(letra_usuario)                                                                        # Ela será removida, usando a letra de entrada do usuário
                print('')                                                                                               # Printa a letra na tela
                print(palavra_valida())
            else:
                vidas = vidas - 1                                                                                       # Se o usuário errar, perde uma vida e printa a letra já usada
                print('\nSua letra,', letra_usuario, 'não está na palavra.')

        elif letra_usuario in letras_usadas:                                                                            # Aqui verifiquei se a letra já foi utilizada e para não ser um DARK SOULS da vida, ele informa que ele já utilizou a letra
            print('\nVocê já utilizou esta letra, por favor advinhe outra.')

        else:                                                                                                           # Aqui é se o Filho de uma puta digita um "%" ou "?"
            print('\nEsta não é uma letra válida.')


    if vidas == 0:                                                                                                      # Aqui pensei em colocar o "len(wrd_letras) mas acho que essa condição já ta boa
        print(bonequinho[vidas])                                                                                        # Aqui é o bonequinho
        print('Perdeu filho da puta, vai estudar português caralho! Esta era a porra da palvra válida: ', palavra_valida())
    else:
        print('AÊee CUZÃO, tu acertou a palavra: ',palavra_valida(), '!!')


if __name__ == '__main__':
    jogo()




