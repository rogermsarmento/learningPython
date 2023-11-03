#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def fibonacci(quant, sequencia=(0, 1)):
    # Condição de parada: a tupla sequencia deve ter o mesmo tamanho de quant.
    if len(sequencia) == quant:
        return sequencia
    return fibonacci(quant, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros numeros de fibo.
    for fib in fibonacci(20):
        print(fib)

'''python
a = (1, 2)
b = (3, 4)
type(a)
type(b)
a + b
(1, 2, 3, 4)
'''
