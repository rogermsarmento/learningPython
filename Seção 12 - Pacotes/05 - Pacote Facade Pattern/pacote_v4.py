'''
Vamos importa a função diretamente sem 
a necessidade de importa um móidulo.
Podemos acessar o pacote, o módulo e importar a função.
'''

from pacote1.modulo1 import soma
from pacote2.modulo1 import sub as subtracao


print(soma(2, 5))
print(subtracao(9, 8))
