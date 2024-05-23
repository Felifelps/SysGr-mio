<p align="center">
    <img src="/assets/icon.png" alt="Logo" width=200 height=200>
</p>

# SysGremio

O SysGremio é uma urna eletrônica desenvolvida inicialmente no segundo ano do curso técnico em informática para ser utilizada durante a eleição do Grêmio da escola.

## Funcionalidades

- Configuração de chapas;
- Votação segura;
- Som de aviso após votação;
- Geração de arquivo com os resultados após a votação.

## Tecnologias usadas

- Python;
- Framework Flet;
- Bcrypt, para criptografia;
- Peewee, como *Object Relational Mapping*;
- Dotenv.

## Instalação

Para instalar o projeto, siga os seguintes passos:

1. [Instale o python](https://www.python.org/downloads/) mais recente em sua máquina
2. Clone o projeto:

    ```
    git clone https://github.com/Felifelps/SysGremio SysGremio
    ```

3. Entre na pasta do projeto, crie e ative um ambiente virtual:

    - Windows:
        ```
        cd SysGremio
        python -m venv venv
        venv\Scripts\activate
        ```
    - Linux/MacOS:
        ```
        cd SysGremio
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

5. Agora, rode o seguinte comando para gerar sua senha:

    ```
    python generate_env.py <sua-senha>
    ```

6. Para iniciar o projeto, rode o seguinte comando:

    ```
    flet run app.py
    ```

Ou tente instalar para windows com [o pacote .msi](/windows).

## Contribuição

Fique à vontade para fazer Forks e várias Pull Requests. Estou aberto a sugestões e melhorias.