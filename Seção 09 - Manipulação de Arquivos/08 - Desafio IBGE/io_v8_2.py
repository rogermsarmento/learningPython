#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV')
        dados = entrada.read().decode('latin1')
        print('Download Completo!')
        for cidades in csv.reader(dados.splitlines()):
            print(f'{cidades[2]}: {cidades[8]}: {cidades[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
