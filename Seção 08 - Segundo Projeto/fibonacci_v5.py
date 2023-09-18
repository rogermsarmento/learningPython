#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''
'''
(a, b) = (b, a) - SWAP
a, b = b, a - SWAP
'''


def fibonacci(lim):
    result = [0, 1]

    while result[-1] < lim:
        result.append(sum(result[-2:]))
    return result


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
