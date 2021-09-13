from random import randint, choice


def gerador_senha():
    v1 = choice(['@', '#', '_'])
    v2 = ''
    v3 = choice(['sE','deE','dEs','taR'])
    v4 = ''

    for i in range(0,4):
        v2 += str(randint(0, 9))

    for i in range(0,2):
        v4 += str(randint(0, 9))

    senha = v1 + v2 + v3 + v4

    return senha
