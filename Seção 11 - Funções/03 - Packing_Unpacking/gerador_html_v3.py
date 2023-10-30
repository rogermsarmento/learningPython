#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    # Não precismos nem de generatuions e nem de list compreheson
    # lista = ''.join(f'<li>{item}</li>' for item in itens)
    # Usando os () temos um GENERATION
    # lista = ''.join((f'<li>{item}</li>' for item in itens))
    # Usando os [] temos uma LIST COMPREHESION
    lista = ''.join([f'<li>{item}</li>' for item in itens])
    return f'<ul>{lista}</ul>'
    '''
    Nesta função temos um generation que para cada item que recebermos da 
    minha tupla eu vou percorrer esse item e ele vai gerar um <li>.
    A string gerarda pelo generation vai sofrer um operação de join com a 
    string vazia e eu vou gerar minha lista.
    Essa string gerada vai para dentro da <ul>.
    ```
    '''


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    # nesse ponto invertemos a ordem dos parâmetros!
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
