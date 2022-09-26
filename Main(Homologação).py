#Jogo da Forca - Project by Eduardo Santos & Matheus Santos
#ver 1.0 / rev 0.1
#----------------------------------------------------------
import random
from Import import lives_visual_dict as bonequinho
from palavras import Palavras
import string

print('-=' * 20)
print(' ' * 10, 'JOGO DA FORCA')
print('-=' * 20)
print()

''' CÓDIGO DO MATHEUS
wrd = random.choice(palavras)                                                                                           #wrd = word
print(wrd.upper())
wrdlist = list(wrd)                                                                                                     # Aqui fiz uma lista das letras da palavra que a variavel "wrd" resgatou de palavras, isso permite trabalhar com indices para cada letra e ajuda a por na ordem certa
wrdlistcopia = wrdlist[:]   # Aqui fiz uma copia da lista acima para nao sobrescrever os valores da primeira lista quando o usuario estiver jogando, pois isso pode acabar atrapalhando o algoritmo de rodar

lacunas = []            # }
for l in wrdlistcopia:  # } Neste pequeno loop estou criando uma lista com varios tracos ( " - ") que serao o indicador de quantas letras a palavra tem mas sem revela-la ao jogador
    lacunas.append('_') # }

def validacao(): #Aqui chamei uma funcao para fazer a validacao das letras
    global fim # Aqui estou atribuindo uma variavel global fim pra ser usada fora desse loop
    global chances # Mesma coisa que acima
    while fim == 's': #Aqui comeca um loop que se encerra quando o jogo termina ou por acertou ou fim das vidas
        letra_usuario = input('Digite uma letra: ') # Input de letra do usuario
        count = wrdlistcopia.count(letra_usuario)   # Aqui sera feita a contagem de quantas vezes a letra que o usuario inputou se repete na palavra
        if letra_usuario not in wrdlistcopia:       # Validando o input do usuario
            chances -= 1 #Caso o usuario digite uma letra que nao se encontra na palavra essa variavel vai tirando o numero de chances dele
            print(f'Voce errou, restam {chances} chances') #Print avisando quando o usuario errou
        else: #Bloco de codigo caso ele acerte alguma letra da palavra
            lacunas[wrdlistcopia.index(letra_usuario)] = letra_usuario # Aqui estou simplesmente reatribuindo o valor do indice de lacunas para a letra que o usuario inputar
        if count > 1: # Aqui estou considerando caso o numero de letras que ele digitou se repita
            try: # Aqui peco pro algoritmo rodar um try/except e evitar mensagens de erro
                for i, v in enumerate(wrdlistcopia): # Aqui o algoritmo vai passar pelo indice de cada letra na lista
                    lacunas[wrdlistcopia.index(letra_usuario, i)] = letra_usuario # Aqui fiz o mesmo processo que na linha 38 porem se a letra se repetir, o algoritmo vai buscar qual o indice da proxima letra que se repete a partir do indice que o i esta iterando, ja que o metodo .index retorna apenas o primeiro indice do valor escolhido.
            except ValueError: # Except bem auto-explicativo
                pass
        print(lacunas) # Aqui ele vai printar conforme o usuario for acertando as letras
        if lacunas == wrdlistcopia: # Aqui um if do que fazer caso o game termine por acerto
            fim = 'n'
        elif chances == 0: #Aqui o elif caso termine por erro
            fim = 'n'


fim = 's' #Exemplo do algoritmo rodando
chances = 6
while fim == 's' or chances > 0:
    validacao()
'''



def palavra_valida(Palavras):
    wrd = random.choice(Palavras)
    while '-' in wrd or ' ' in wrd:
        wrd = random.choice(Palavras)

    return wrd.upper()


def jogo():
    wrd = palavra_valida(Palavras)                                                                                      # Chamando a função PALAVRA_VALIDA
    wrd_letras = set(wrd)                                                                                               # Criando a variável para usar o set para evitar palavras duplicadas
    alfabeto = set(string.ascii_uppercase)                                                                              # Variável para atribuir as letras da palavra escolhida como capslock
    letras_usadas = set()                                                                                               # Variável para as letras usadas, quero mostrar quais eles já digitou

    vidas = 7                                                                                                           #Quantidade de vidas, assim já puxo daqui qual das imagens da lista do outro arquivo


    while len(wrd_letras) > 0 and vidas > 0:                                                                            # Condição óbvia kkkkk


        print('Você tem', vidas, 'vidas sobrano e você já utilizou estas letras: ', ' '.join(letras_usadas))            # Usei o join para ele não separar as letras por ' '. Ficará assim: # ' '.join(['a', 'b', 'cd']) --> 'a b cd'


        lista_palavras = [letra if letra in letras_usadas else '-' for letra in wrd]                                    # Aqui criei uma variável e fiz uma pequena função. Uma lista de letras para as letras já usadas
        print(bonequinho[vidas])                                                                                        # Aqui mostrará a parte do boneco baseado na quantidade de vidas!
        print('Palavra atual: ', ' '.join(lista_palavras))                                                              #Mesmo princípio do primeiro JOIN

        letra_usuario = input('Adivinhe a letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:                                                                   # Usei a subtração para verificar se a letra inserida não está entre as duas variáveis
            letras_usadas.add(letra_usuario)                                                                            # A letra inserida vai para as letras usadas
            if letra_usuario in wrd_letras:                                                                             # Se a letra estiver dentro da palavra selecionada
                wrd_letras.remove(letra_usuario)                                                                        # Ela será removida, usando a letra de entrada do usuário
                print('')                                                                                               # Printa a letra na tela

            else:
                vidas = vidas - 1                                                                                       # Se o usuário errar, perde uma vida e printa a letra já usada
                print('\nSua letra,', letra_usuario, 'não está na palavra.')

        elif letra_usuario in letras_usadas:                                                                            # Aqui verifiquei se a letra já foi utilizada e para não ser um DARK SOULS da vida, ele informa que ele já utilizou a letra
            print('\nVocê já utilizou esta letra, por favor advinhe outra.')

        else:                                                                                                           # Aqui é se o Filho de uma puta digita um "%" ou "?"
            print('\nEsta não é uma letra válida.')


    if vidas == 0:                                                                                                      # Aqui pensei em colocar o "len(wrd_letras) mas acho que essa condição já ta boa
        print(bonequinho[vidas])                                                                                        # Aqui é o bonequinho
        print('Perdeu filho da puta, vai estudar português caralho! Esta era a porra da palvra válida: ', wrd)
    else:
        print('AÊee CUZÃO, tu acertou a palavra: ', wrd, '!!')


if __name__ == '__main__':
    jogo()





