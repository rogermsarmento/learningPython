#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def log(function):
    # Função que sera usada como decotaror
    # Vamos passar a função pra ela,
    # fazemos coisas antes e depois
    # no meio eu faço a chamada da função
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da Função: {function.__name__}')
        print(f'Argumentos Posicionais: {args}')
        print(f'Argumentos Nomeados: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada de Resultado: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


# @log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    soma(5, 7)  # Só chama o LOG
    print(sub(5, y=7))
