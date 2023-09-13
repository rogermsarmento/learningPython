# Percorrendo uma String
palavra = 'paralelepípedo'
for letra in palavra:
    # o segundo paramento indica que o final de letra será um vírgula,
    # podemos usar \n, " " e outros.
    print(letra, end=',')
print('Fim')

# Percorrendo uma Lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)
    # print(nome, end=" ")

# Percorrendo uma Lista vom enumerate
for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)
    # print(f'posicao + 1', nome)
    # print(f'{posicao + 1})', nome)

# Percorrendo uma Tupla
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

# Percorrendo um Set
# for letra in set('Criando um set')
for numero in {1, 2, 3, 4, 5, 6}:  # Set literal
    print(numero)
