#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''

import csv

with open('ibge.csv') as entrada:
    for itens in csv.reader(entrada):
        # print('Nome: {3}, Idade:{4}'.format(*itens))
        print(itens)
