#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


generator = (i ** 2 for i in range(10) if i % 2 == 0)

for num in generator:
    print(num)


# print(next(generator))  # saida 0
# print(next(generator))  # saida 4
# print(next(generator))  # saida 16
# print(next(generator))  # saida 36
# print(next(generator))  # saida 64
# print(next(generator))  # erro
