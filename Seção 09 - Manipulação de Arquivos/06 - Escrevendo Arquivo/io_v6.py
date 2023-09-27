#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''
with open('pessoas.csv') as arquivo:  # Abre pessoas.csv
    with open('pessoas.txt', 'w') as saida:  # Abre pessoas.txt
        # O WITH garante que o arquivo será fechado no final.
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} - Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo Fechado!')

if saida.closed:
    print('Saida Fechado!')
