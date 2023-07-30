# App GymForce

## 💻 Sobre o projeto
- <p>Projeto em desenvolvimento...</p>
- <p>Academia Digital 🚀</p>

## 🛠 Tecnologias

- Python
- Django


### Pré-requisitos

* Necessario ter o python instalado na maquina para rodar o projeto
* A versão do Python utilizada foi a 3.9, recomendo usar a mesma.
* Projeto em desenvolvimento.

Instruções para rodar o app:

Após clonar este projeto, execute no terminal na pasta do projeto os seguintes comandos:

Linux:

<code>python3 -m venv venv</code>

Windows: 

<code>python -m venv venv</code>


Isso ira criar um ambiente virtual de desenvolvimento para seu interpretador python.

Após criar o ambiente virtual é preciso ativalo através do comando:

Linux

<code>source venv/bin/activate</code>

Windows

<code>venv\Scripts\Activate</code>

Agora vamos instalar o django:

<code>pip install django</code>

Instale também a biblioteca para converter HTML em PDF para que você consiga gerar o relatorio em PDF. Por padrão a biblioteca weasyprint usa algumas funcões da biblioteca pillow, sendo necessario também instalar a pillow.

<code>pip install weasyprint</code>
<code>pip install pillow</code>

Outra biblioteca necessaria é a que gerencia a conexão com o banco de dados postgres:

<code>pip install psycopg2</code>

* Lembrando que é necessário ter instalado o postgresql em sua maquina, rodando na porta padrão 5432, com usuario postgres e senha admin. Além disso precisa ser criado um banco de dados com o nome de gymforce;

### Para quem está no windows é preciso executar o seguinte passo para conseguir gerar o relatório em PDF:

Baixe o GTK3 pelo site:

<code>https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases</code>

* Apos baixar, instale e reinicie a maquina.

Após ter o django instalado é hora de rodar o projeto:

<code> python3 manage.py runserver</code>

Acesse a url <code>http://localhost:8000/</code>
