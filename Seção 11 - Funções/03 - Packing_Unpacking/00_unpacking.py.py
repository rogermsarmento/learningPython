#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 3, 4))

    # packing - empacotando os paramentos para
    # dentro de uma tupla e passado para função.
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))

    # unpacking - pegamos um tupla e passamos
    # como parâmetro para função.
    tupla_nuns = (1, 10, 100)
    print(soma_n(*tupla_nuns))

    lista_nuns = [1, 10, 100]
    print(soma_n(*lista_nuns))
