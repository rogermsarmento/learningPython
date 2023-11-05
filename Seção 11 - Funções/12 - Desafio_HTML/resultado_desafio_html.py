#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

'''
1º - Verificar se recebemos dentro dos argumentos 
nomeados a propriedade html_class, para que consigamos 
subistituir ela pela class.

2º - Gerar o body da tag.


'''


def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        # Subistituindo html_cass por class
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f'{k}="{v}" ' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Learning Python, por'),
            tag('strong', 'Roger M Sarmento', id='rms'),
            tag('span', ' e '),
            tag('strong', 'Fulano de tal', id='ft'),
            tag('span', '.'),
            html_class='alert')
    )
