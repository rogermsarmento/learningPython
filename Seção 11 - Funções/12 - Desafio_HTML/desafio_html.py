#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


def tag(tag, *args, **kwargs):
    pass


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
