#! python

"""
Shebang no Ambiente Windows

O conceito do Shebang funciona apenas nos ambientes Linux/MacOS. 

SUSTENIDO!/usr/local/bin/python3

A documentação do Python explica que não há suporte oficial para 
Shebang no Windows. Para proceder corretamente nas próximas aulas 
sem problemas utilizando Windows basta substituir a linha do 
shebang utilizada pelo professor pelo seguinte código: 

'SUSTENIDO! python'

Dessa forma vai funcionar normalmente no Windows da mesma forma 
que funciona nos outros ambientes. Caso queiram ler mais a 
respeito, está tudo dentro da documentação do Python no 
seguinte link: https://docs.python.org/3/using/windows.html
"""


pi = 3.14159
raio = 15.3
print('Área do círculo', pi * raio ** 2)


"""
Nas próximas aulas o professor irá executar um 
código no terminal com a seguinte sintaxe:

./nomeDoArquivo.py

No caso acime é necessário ar permissão ao arquivo.
sudo chmod u+x "nome do arquivo"

No entanto, essa sintaxe não vai funcionar em todos os sistemas. 
Se for o seu caso, basta usar a seguinte sintaxe:

python nomeDoArquivo.py
"""
