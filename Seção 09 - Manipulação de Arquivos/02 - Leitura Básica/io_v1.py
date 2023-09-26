#! python
'''
SUSTENIDO!/usr/local/bin/python3
'''

arquivo = open(
    r'..\01 - Criando Arquivos CSV\Teste de Sistema com CSV\pessoas.csv')
# Capaturei o conteudo do arqwuivo e coloquei dentro de dados.
dados = arquivo.read()
arquivo.close()  # Liberei os recursos do sistema que estavam em uso.
print("1º -------------------------------")
# Divida uma string em uma lista onde cada linha é um item da lista:
for registro in dados.splitlines():
    print(registro)
print("\n")
print("2º -------------------------------")
for registro in dados.splitlines():

    print(registro.split(','))  # Separa o registro em duas parte.
    # Será criado uma lista que tem como primeiro elemento o nome
    # e o segundo a idade.
print("\n")
print("3º -------------------------------")
for registro in dados.splitlines():
    # Com o * os valores são passados como argumentos.
    # Os itens de registro.split(',') serão passados como argumentos.
    print(*registro.split(','))

print("\n")
print("4º -------------------------------")
for registro in dados.splitlines():

    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

'''
Então precisamos mudar de diretório via estes símbolos

Vamos então descrever cada um deles:

../ – Com este símbolo podemos voltar um diretório, ou seja, se você está em 
um diretório x dentro de y, com os .. você voltaria para o y, podendo acessar 
os arquivos que estão a partir de lá;

./ – Acessando arquivos desta forma você está querendo acessar os arquivos que 
estão no diretório atual, ou seja, você tem acesso a todos os arquivos que 
estão na pasta deste arquivo;

/ – Utilizando o símbolo de barra você está indo até a raiz do projeto, 
ou seja, onde você terá acesso a todas as pastas/diretórios e 
arquivos do mesmo;

../pasta1 – Com esta instrução, você está voltando um diretório e acessando 
a pasta1;

/css/index.css – Com esta instrução você está acessando a  raiz do projeto, 
depois a pasta de arquivos CSS e o arquivo de CSS chamado index.css;

/pasta1/pasta2 – A partir da raiz do projeto, você está acessando a pasta1 e 
depois a pasta2;

../../ – Com esta sequência você está voltando duas pastas/diretórios;

Basicamente são estas as sequências/comandos mais utilizados ao acessarem 
arquivos e pastas do projeto
'''
