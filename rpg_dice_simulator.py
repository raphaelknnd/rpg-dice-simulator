'''Trata-se de um simulador de dador de rpg que receberá uma entrada do usuário no formato "1d20" que especifica a quantidade de jogadas
e o dado que será rolado.'''
import random

dice_hall = (4, 6, 8, 10, 12, 20, 100)

# função que vai identificar o número de jogadas e o dado a ser jogado
def identify(play):
    # a letra 'd' será a nossa referência para separar as informações
    number_of_plays = int(play[:play.index('d')])
    dice = int(play[play.index('d') + 1:])

    if dice not in dice_hall:
        return 'Dado não existente. Tente novamente!'

    return [number_of_plays, dice]

def dice_roll(roll):
    identified = identify(roll)

    if type(identified) == type('str'):
        return identified

    x = 0
    init = 1
    result = []

    while(x < identified[0]):
        if identified[1] == 100:
            init = 0
            value = random.randrange(init,10 + init) * 10
        else:
            value = random.randrange(init,identified[1] + init)

        result.append(value)
        x += 1

    return result


# execução
while(True):
    # a exceção garante que o código não caia em um erro na sintaxe de entrada ex: 1d20
    try:
        play = input("Jogada[ex: 2d20]: ")

        if play == '0':
            break
        else:
            print(dice_roll(play))
    except ValueError:
        print('Opa algo deu errado, temte novamente!\n')