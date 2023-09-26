#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''

arquivo = open(
    r'..\01 - Criando Arquivos CSV\Teste de Sistema com CSV\pessoas.csv')

for registro in arquivo:
    print('Nome: {} - Idade: {}'.format(*registro.split(',')))
    # print('Nome: {} - Idade: {}'.format(*registro.split(',')), end='')
    # Sem o end no final ele quebra a linha pq já vem com \n por padrão.
arquivo.close

# Nesse programa o python vai lendo o arquivo sobre demanda, ou seja,
# ele envia o que esta sendo lido e não o arquivo completo.
# no programa passado ele lia o arquivo completo e fechava a conexão.
