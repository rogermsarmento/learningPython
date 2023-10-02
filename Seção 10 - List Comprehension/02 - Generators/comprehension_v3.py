#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

# Gerador de numeros que consome menos memoria do que o
# list comprehension que já gera a lista completa.
# Generator gera os dados sob demanda.

# Sem comprehension
generator = []
for i in range(11):
    if i % 2 == 0:
        generator.append(i ** 2)

print(generator)

# com comprehension

generator = (i ** 2 for i in range(11) if i % 2 == 0)
print(next(generator))  # saida 0
print(next(generator))  # saida 4
print(next(generator))  # saida 16
print(next(generator))  # saida 36
print(next(generator))  # saida 64
# print(next(generator))  # erro
