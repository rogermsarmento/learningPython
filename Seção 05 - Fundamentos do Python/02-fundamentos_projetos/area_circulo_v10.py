#!/usr/local/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    # Recebe o raio pelo cmd.
    # Então podemos fazer ./"nomedo aroo arquivo" <raio>
    # argv[0] = nome do script
    # argv[1] = primeiro parâmetro
    area = circulo(raio)
    print('Área do círculo', area)
