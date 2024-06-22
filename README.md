<p align="center">
    <img src="/assets/icon.png" alt="Logo" width="200" height="200">
</p>

# SysGremio

SysGremio is a simple voting app developed initially in the second year of the technical course in computer science to help with student council voting.

## Functionalities

- Slate configuration
- Secure voting
- Alert sound after voting
- Generation of a result file at the end of the voting

## Technologies

- Python
- Flet
- Bcrypt
- Peewee
- Dotenv

## Installation

To install this project, follow these steps:

1. [Install Python](https://www.python.org/downloads/) on your machine.
2. Clone this project:

    ```shell
    git clone https://github.com/Felifelps/SysGremio SysGremio
    ```

3. In the project directory, create and activate a virtual environment:

    - Windows:

        ```shell
        cd SysGremio
        python -m venv venv
        venv\Scripts\activate
        ```

    - Linux/MacOS:

        ```shell
        cd SysGremio
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Install the project requirements:

    ```shell
    pip install -r requirements.txt
    ```

5. Set your password by running:

    ```shell
    python generate_env.py
    ```

6. Run the project with:

    ```shell
    flet run app.py
    ```

If you are on Windows, install the .msi package from [here](https://github.com/Felifelps/SysGremio/releases/tag/windows).

## Contribution

Fork this repo and make a pull request with your changes, and I'll review it as soon as possible.
