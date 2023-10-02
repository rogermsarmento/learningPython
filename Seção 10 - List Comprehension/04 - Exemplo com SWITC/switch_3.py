#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        tuple(range(2, 7)): 'Dia de Semana',
    }
    dia_escolhido = (tipo for num, tipo in dias.items() if dia in num)
    return next(dia_escolhido, '** dia inválido!')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')


# Compare esse código com:
"""
def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
"""
