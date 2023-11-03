#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

# Nos programas de fibonacci passamos uma
# tupla como params. Pq uma tupla?
# Pq ela é imutavel.
# Agora vamos ver o problema de params
# padrão mutaveis, usanod uma lista.

# sequencia é um params padrão que já tem um valor default
# ou seja, se não for passar valor para sequencia automatcamente
# ele recebe (0, 1).

'''python
a = (1, 2)
b = (3, 4)
type(a)
type(b)
a + b
(1, 2, 3, 4)
Soma de tuplas é uma concatenação.
(sum(sequencia[-2:]),) a virgula serve para dizer que eles são uma tupla
'''


def fibo(quant, sequencia=(0, 1)):
    if len(sequencia) == quant:
        return sequencia
    return fibo(quant, sequencia + (sum(sequencia[-2:]),))

# o uso de mutaveis como defualt tem uma armadilha.


def fibonacci(sequencia=[0, 1]):
    sequencia.append(sequencia[-1] + sequencia[-2])
    # nessa linha estamos alterando o valor default.
    return sequencia

# solução temporaria


def fibonacci_tupla(sequencia=(0, 1)):
    # sequencia.append(sequencia[-1] + sequencia[-2])
    # nessa linha estamos alterando o valor default.
    return sequencia + (sequencia[-1] + sequencia[-2],)


if __name__ == '__main__':
    # for fib in fibonacci(5):
    #    print(fib)
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
