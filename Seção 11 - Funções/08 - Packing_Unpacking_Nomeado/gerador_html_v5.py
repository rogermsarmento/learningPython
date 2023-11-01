#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''
'''
Nesta versão passaremos para tag_bloco e tag_lista uma 
serie de parâmetros variáveis nomeados e esses params
vão servir para adicionar nas duas tags: <ul> e sapn ou div.
'''

# Esse parametro recebe a lista de atributos informados

bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = get_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {get_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))

    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))

    # print(tag_lista('item 1', 'item 2'))
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))

    # print(tag_bloco, 'Sábado', 'Domingo', classe='info', inline=True)
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo',
                    classe='info', inline=True))

    # V5 comça aqui!
    print(tag_bloco(tag_lista, 'item 1', 'item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
