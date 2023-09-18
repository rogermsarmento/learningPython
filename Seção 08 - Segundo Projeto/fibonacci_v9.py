#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def fibonacci(quant, sequencia=(0, 1)):
    # Condição de parada: a tupla sequencia deve ter o mesmo tamanho de quant.
    # Operador TERNÁRIO
    return sequencia if len(sequencia) == quant else \
        fibonacci(quant, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros numeros de fibo.
    # for fib in fibonacci(20, (4, 5)):
    # dessa forma podemos dizer os valores iniciais.
    i = 1
    for fib in fibonacci(10):
        print(f'{i}:{fib}')
        i += 1
