#!/usr/local/bin/python3
from math import pi


# Com esse teste o modulo somente será executado se ele fizer parte do main.
# Desta forma quando o import "nome do arquivo" for chamado o script não
# será executado automaticamente.
if __name__ == '__main__':
    raio = input('Informe o raio: ')
    print('Área do círculo', pi * float(raio) ** 2)
