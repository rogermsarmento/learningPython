#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def todos_params(*args, **kwargs):
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    # 'a', 'b', 'c' são parms posicionais e foram para args.
    # ou seja, foi feito um packing para uma tupla e esta
    # tuplas tem os 3 elementos.

    todos_params(1, 2, 3, legal=True, valor=12.99)
    # Neste exemplo teremos uma tupla com os 3 primeiros
    # parâmetros e um dict com os outros 2.

    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)

    # ATENçÃO - Não podemos ter parametros nomeados e depois posicionais
    # todos_params(primeiro='Joao', 'Maria')
    # Solução
    todos_params(primeiro='Joao', segundo='Maria')
    todos_params('Maria', primeiro='Joao')
