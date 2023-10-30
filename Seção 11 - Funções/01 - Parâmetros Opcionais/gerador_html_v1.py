#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


'''
classe='sucesso': siguinifica que se não for passado nada
por padrão o argumento será sucesso.
'''

if __name__ == '__main__':
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'

# o ==\ é parta quebrar a linha.

    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'

    print(tag_bloco('bloco'))
