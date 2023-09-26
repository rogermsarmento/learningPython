#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''
try:
    arquivo = open(
        r'..\01 - Criando Arquivos CSV\Teste de Sistema com CSV\pessoas.csv')

    for registro in arquivo:
        print('Nome: {} - Idade: {}'.format(*registro.strip().split(',')))
        # print('Nome: {} - Idade: {}'.format(*registro.split(',')), end='')
        # Sem o end no final ele quebra a linha pq já vem com \n por padrão.

except IndexError:  # Isso será estudado mais a frente!
    # Retire o asterisco e veja que o erro não aparece!
    pass

finally:
    print('Finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo Fechado!')

# Nesse programa o python vai lendo o arquivo sobre demanda, ou seja,
# ele envia o que esta sendo lido e não o arquivo completo.
# no programa passado ele lia o arquivo completo e fechava a conexão.


'''
Comndo strip() - retira os espaçõs nas bosdas.
'     teste abc     '
'     teste abc     '.strip() = 'teste abc'
Contudo ele não remove espações no meio.
'00000      000000'.strip() = nada avcontece, mas
'00000      000000'.strip('0') ele retira os numero 0.
Mas podemos chamar 2 vezes.
'00000      000000 abc      '.strip('0').strip() 
'''
