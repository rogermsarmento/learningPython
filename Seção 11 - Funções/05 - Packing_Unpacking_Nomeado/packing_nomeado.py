#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''
# **kwargs
'''
Neste caso temos varios parâmetros para função f1
que faz o packing e coloca tudo dentro do dict.

'''


def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='Sena',
                 segundo='Prost',
                 terceiro='Mansel')
