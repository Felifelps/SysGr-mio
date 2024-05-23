# SysGremio

O SysGremio é uma urna eletrônica desenvolvida inicialmente no segundo ano do curso técnico em informática.

## Funcionalidades

- Configuração de chapas;
- Votação segura;
- Som de aviso após votação;
- Geração de arquivo com os resultados após a votação.

## Tecnologias usadas

- Python
- Framework Flet
- Bcrypt, para criptografia
- Peewee, como *Object Relational Mapping*
- Dotenv

## Instalação

### Windows

Para instalar o projeto no Windows, siga os seguintes passos:

1. [Instale o python](https://www.python.org/downloads/) mais recente em sua máquina
2. Clone o projeto:
    ```
    git clone https://github.com/Felifelps/SysGremio SysGremio
    ```
3. Entre na pasta do projeto, crie e ative um ambiente virtual:
    ```
    cd SysGremio
    python -m venv venv
    venv\Scripts\Activate
    ```
4. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```
5. Após as instalações, rode o seguinte comando:
    ```
    flet run app.py
    ```

Ou tente instalar o pacote .msi na pasta `/windows`.

### Linux e MacOS

O projeto ainda não está 100% disponível para Linux ou MacOS.

## Contribuição

Fique à vontade para fazer Forks e várias Pull Requests. Estou aberto a sugestões e melhorias.