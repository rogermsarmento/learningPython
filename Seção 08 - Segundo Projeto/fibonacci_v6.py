#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def fibonacci(quant):
    result = [0, 1]

    while True:
        result.append(sum(result[-2:]))
        # Condição de parada: o tamanho do array não pode
        # ultrapassar o valor de quantidade.
        if len(result) == quant:
            break
    return result


if __name__ == '__main__':
    # Listar os 20 primeiros numeros de fibo.
    for fib in fibonacci(20):
        print(fib)
