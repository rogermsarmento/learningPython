#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

'''
Neste exemplo o parâmetro inline serve ´para definir 
se teremos uma div ou um span. Usaremos um op ternario.
'''

'''
classe='sucesso': siginifica que se não for passado nada
por padrão o argumento será sucess.
'''


def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    # nesse ponto invertemos a ordem dos parâmetros!
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, texto='inline'))
    print(tag_bloco('falhou', classe='error'))
