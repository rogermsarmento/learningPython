'''
A função main() pode até ser chamada a partir 
do modulo principal, mas não podemos chamar diretamente
no módulo. Então verificamos o nome do módulo, 
se for o principal aí sim executamos o main() 
'''


def main():
    print(f'Executando o Main() no módulo {__name__}')


if __name__ == '__main__':
    main()
