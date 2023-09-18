#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def fibonacci(lim):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while ultimo < lim:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(20000)
