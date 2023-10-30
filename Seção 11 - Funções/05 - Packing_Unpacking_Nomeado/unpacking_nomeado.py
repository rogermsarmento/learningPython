#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''
# **kwargs
'''
Neste caso estamos pegando o dict e desempacotado ele
e passando como parâmetro para uma função que recebe
3 parâmetros
'''


def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    podium = {'primeiro': 'Sena',
              'segundo': 'Prost',
              'terceiro': 'Mansel'}
    resultado_f1(**podium)
