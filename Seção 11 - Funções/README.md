# SEÇÃO 11 - Funções

Em Python, uma função é um bloco de código reutilizável que realiza uma tarefa específica. Ela é definida usando a palavra-chave **def** e, normalmente, aceita argumentos (parâmetros) como entrada e pode retornar um valor como saída. A sintaxe básica para definir uma função em Python é a seguinte:

```
def nome_da_funcao(argumento1, argumento2, ...):
    # Corpo da função
    # Executa uma tarefa ou cálculo
    return valor_retornado
```

Aqui está uma explicação dos elementos chave em uma definição de função em Python:

- def: É a palavra-chave usada para declarar uma função.

- nome_da_funcao: Este é o nome dado à função. Deve seguir as regras de nomenclatura de variáveis em Python.

- argumento1, argumento2, ...: São os argumentos (parâmetros) que a função pode aceitar. Eles são opcionais e podem ser usados para passar informações para a função.

- : (dois-pontos): Indica o início do corpo da função.

- Corpo da função: É onde você escreve o código que a função executará quando for chamada. Pode conter uma ou várias instruções.

- return: A palavra-chave return é usada para especificar o valor que a função retornará quando for chamada. Uma função pode ou não ter uma instrução de retorno. Se ausente, a função retornará None.

Aqui está um exemplo simples de uma função que soma dois números:

```
def soma(a, b):
    resultado = a + b
    return resultado
```

Você pode chamar essa função da seguinte forma:

```
resultado_da_soma = soma(3, 4)
print(resultado_da_soma)  # Isso imprimirá 7
```

As funções em Python são fundamentais para a organização e reutilização de código e desempenham um papel crucial na modularização de programas complexos.

## Parâmetros

Os parâmetros em uma função em Python podem ser passados de duas maneiras diferentes: como argumentos nomeados (ou palavras-chave) e como argumentos posicionais. A principal diferença entre eles está na forma como os argumentos são associados aos parâmetros da função.

1. Parâmetros Posicionais:

- Os argumentos posicionais são passados para a função na ordem em que os parâmetros da função foram definidos.
- Eles correspondem aos parâmetros da função com base na ordem em que são fornecidos.
- Se a ordem dos argumentos posicionais estiver incorreta, a função pode não funcionar conforme o esperado.

Exemplo:
```
def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")

saudacao("Maria", "Olá")  # Passagem de argumentos posicionais

```

2. Parâmetros Nomeados:

- Os argumentos nomeados são associados aos parâmetros da função usando o nome do parâmetro.
- Eles não dependem da ordem em que os parâmetros foram definidos na função, pois são identificados por seus nomes.
- Isso torna o código mais legível e menos suscetível a erros quando se trabalha com funções que têm muitos parâmetros.
Exemplo:

```
def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")

saudacao(mensagem="Olá", nome="Maria")  # Passagem de argumentos nomeados

```

No exemplo acima, a ordem dos argumentos nomeados foi trocada em relação à ordem dos parâmetros na definição da função, mas o código ainda funciona conforme o esperado, porque os argumentos são associados aos parâmetros pelos nomes.

A escolha entre argumentos posicionais e nomeados depende das necessidades do seu código. Argumentos posicionais são úteis quando você tem apenas alguns parâmetros e a ordem é clara. Argumentos nomeados são úteis quando você tem muitos parâmetros ou quando a ordem pode ser ambígua, pois tornam o código mais legível e menos suscetível a erros. Geralmente, uma combinação de ambos é usada em diferentes situações, dependendo dos requisitos de cada função.

Tambem existem os parâmetros:
- ***args**: gera um tupla.
- ****kwargs**: gera um dict.