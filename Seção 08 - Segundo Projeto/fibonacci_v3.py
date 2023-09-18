#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''
'''
(a, b) = (b, a) - SWAP
a, b = b, a - SWAP
'''


def fibonacci(lim):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while ultimo < lim:
        # com isso não precisamos da variável próximo.
        penultimo, ultimo = ultimo, penultimo + ultimo
        # proximo = penultimo + ultimo
        # print(proximo, end=',')
        print(ultimo, end=',')
        # penultimo = ultimo
        # ultimo = proximo


if __name__ == '__main__':
    fibonacci(20000)
