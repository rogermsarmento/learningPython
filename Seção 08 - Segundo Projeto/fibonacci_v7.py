#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def fibonacci(quant):
    result = [0, 1]

    # for i in range(2, quant): ou for _ in range(2, quant):
    for i in range(quant-2):
        result.append(sum(result[-2:]))
    return result


if __name__ == '__main__':
    # Listar os 20 primeiros numeros de fibo.
    for fib in fibonacci(20):
        print(fib)
