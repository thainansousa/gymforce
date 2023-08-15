# WebApp GymForce

## 💻 Sobre o projeto
- <p>Versão 1.0.0</p>
- <p>Academia Digital 🚀</p>
- <p>A finalidade deste projeto é desenvolver e aprimorar os conhecimentos na linguagem <strong>python e framework django.</strong> E torna-lo opensource para que todas as academias que estão começando e não tem dinheiro para contratar um sistema no mercado ou também para professores de Educação Fisica que queiram montar seu negocio consigam ter um sistema gratuito, precisando apenas duma maquina com o python e o postgresql instalado.</p>
- <p>A primeira versão é algo ainda muito "cru", mas pretendo ir evoluindo o sistema até chegar em algo mais "enxuto"</p>
- <p>Na próxima versão pretendo trazer o executavel, pois, ninguem merece está a todo momento rodando comando no terminal kkkkkk.</p>
## 🛠 Tecnologias

- Python
- Django

### Pré-requisitos

* Necessario ter o python instalado na maquina para rodar o projeto.
* Necessario ter o postgresql instalado na maquina.
* A versão do Python utilizada foi a 3.9, recomendo usar a mesma.
* Projeto em desenvolvimento.

### Instruções para rodar o app:

Após clonar este projeto, execute no terminal na pasta do projeto os seguintes comandos:

#### Linux:

<code>python3 -m venv venv</code>

#### Windows: 

<code>python -m venv venv</code>

Isso ira criar um ambiente virtual de desenvolvimento para seu interpretador python.

Após criar o ambiente virtual é preciso ativa-lo através do comando:

#### Linux

<code>source venv/bin/activate</code>

#### Windows

<code>venv\Scripts\Activate</code>

Antes de instalar qualquer dependencia é recomendado fazer a atualização do pip através do comando:

<code>pip install --upgrade pip</code>

#### Agora vamos instalar o django e todas as outras biblioteca:

<code>pip install -r requirements.txt</code>

Este comando ira instalar todas as dependencias listadas no arquivo requirements.txt

* Lembrando que é necessário ter instalado o postgresql em sua maquina, rodando na porta padrão 5432, com usuario postgres e senha admin. Além disso precisa ser criado um banco de dados com o nome de gymforce;

##### Após isso vamos criar um usuaro para acessar o sistema, através do comando:

#### Linux

<code>python3 manage.py createsuperuser</code>

* Será pedido um nome de usuario um email  e uma senha.

* Esse usuario é necessário para ter o primeiro acesso ao sistema. Pois ao rodar o projeto nesta versão atual ele ainda não cria um usuario por padrão.

#### Windows

<code>python3 manage.py createsuperuser</code>

#### <p style="color:#ec5353">Para quem está no windows é preciso executar o seguinte passo para conseguir gerar o relatório em PDF:</p>

1º Baixe o GTK3 pelo site:

<a href="https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases">https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases</a>

2º Apos baixar, instale e reinicie a maquina.

Após isso é hora de rodar o projeto:

#### Linux

<code>python3 manage.py runserver</code>

#### Windows

<code>python manage.py runserver</code>

Acesse a url <code>http://127.0.0.1:8000/</code>

Ou

<code>http://localhost:8000/</code>


#### <p style="line-height: 25px">* Caso não tenha conseguido rodar o projeto, fale comigo no thainandev@gmail.com como assunto <span style="color:#ec5353">"PROBLEMAS GYMFORCE"</span> que irei te ajudar.</p>