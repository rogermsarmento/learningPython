# Instalando o Python no Linux

Os sistemas GNU/Linux mais recentes ja possuem uma versão do Python instalada junto com o sistema operacional. Podemos checar com o seguinte comando:

```
$ which python3
/usr/bin/python3
```

que nos mostra onde o Python padrão do sistema operacional está instalado.

A versão do Python na distribuição Linux Ubuntu 22.04.2 LTS é a 3.10.

Para evitar conflitos com o Python do sistema operacional, sugere-se a instalação de um outro interpretador, que pode ser feita de 2 formas diferentes: através do de gerenciador de pacotes ou de repositórios.

## Instalação por gerenciadores de pacotes

Os gerenciadores de pacotes mais comuns são ```apt-get ```(Debian, Ubuntu) e ```yum ``` (RedHat, CentOS). Caso sua distribuição utilize um gerenciador de pacotes diferente, acesse a página de downloads do Python.

### Debian e Ubuntu
Através do gerenciador de pacotes, é possível instalar versões específicas do Python. No exemplo abaixo, é instalada a versão, por exemplo, 3.9 do Python
```
sudo apt-get install python3.9
```
É possível instalar qualquer outra versão: ```python3.8```, ```python3.9```, ```python.10```

Desta forma, a instalação desta versão específica do Python acima difere da versão padrão do sistema operacional.
```
$ which python3.9
/usr/bin/python3.9

$ which python3
/usr/bin/python3
```

### Instalação por repositório
Os repositórios no GNU/Linux são chamados de PPAs (do inglês Personal Package Archives).

Para adicionar repositórios ao nosso sistema, precisamos de um software chamado ```software-properties-common```, que pode ser instalado com o comando abaixo:
```
sudo apt-get install software-properties-common
```
Habilitada a adição de repositórios ao nosso sitema operacional, podemos agora incluir o repositório que contém o Python. Este repositório é chamado de deadsnakes, cuja página oficial pode ser encontrada neste link.
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
Agora a instalação do Python pode ser feita a partir deste repositório com o comando
```
sudo apt-get install python3.9
```
Da mesma forma, é possível instalar várias versões. Observem que a versão python correspondente à do sistema operacional padrão não está disponível no repositório deadsnakes.

# Instalando o Python 3 no Windows
Para instalar o Python no seu sistema operacional Windows, você precisa baixar o instalador. Acesse o site oficial neste [link](https://www.python.org/downloads/) e clique em download, como mostrado abaixo.

Isso fará o download do Python 3 para sitemas 64 bits. Para o instalador de 32 bits, acesse e selecione o instalador de 32 bits apropriado, como mostrado abaixo.

### Stable Releases

 - Python 3.1-.11 - April 5, 2023 (_Note that Python 3.10.11 cannot be used on Win 7 or earlier._)


 # Instalando o Python no Mac OS X
Verifique se já tem o Python instalado, se você usa macOS 10.2 ou superior, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:
```
$ which python
```
ou
```
$ which python3
```
que deve retornar algo como ```/usr/bin/python```. Isso significa que o Python está instalado nesse endereço.

## Instalação

Antes de fazer a instalação do Python, é preciso fazer a instalação do XCode, que pode ser baixado na App Store, do pacote para desenvolvimento em linha de comando no macOS, command line tools e dos gerenciadores de pacotes pip e homebrew.

Para instalar o command line tools, digite em um terminal:
```
$ xcode-select --install
```
Para instalar o pip, digite em um terminal:
```
$ sudo easy_install pip
```
Para atualizar o pip, digite em um terminal:
```
$ sudo pip install --upgrade pip
```
Para instalar o homebrew, digite em um terminal:
```
$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```
Para instalar o Python 2, digite em um terminal:
```
$ brew install python
```
Para instalar o Python 3, digite em um terminal:
```
$ brew install python3
```