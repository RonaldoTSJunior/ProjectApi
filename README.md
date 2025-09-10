Chat Interativo com Flask e Gemini API
Descrição

Este projeto é um chat interativo em Python utilizando Flask como servidor web e HTML/CSS/JavaScript para a interface.
O sistema permite enviar mensagens e receber respostas da API Gemini, servindo como prática de integração entre back-end e front-end.

Tecnologias utilizadas

Python 3.12

Flask

HTML / CSS / JavaScript

API Gemini

PyInstaller (opcional, para gerar executável)

Estrutura do projeto
N1/
│── app.py              # Código principal em Flask
│── requirements.txt     # Dependências do projeto
│── templates/           # Arquivos HTML
│── static/              # Arquivos CSS e JS

Como executar

Clone este repositório:

git clone https://github.com/RonaldoTSJunior/nome-do-repositorio.git


Acesse a pasta do projeto:

cd nome-do-repositorio/N1


Crie um ambiente virtual (opcional):

python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac


Instale as dependências:

pip install -r requirements.txt


Configure a variável de ambiente com a chave da API Gemini:

set GEMINI_API_KEY="sua_chave_aqui"      # Windows
export GEMINI_API_KEY="sua_chave_aqui"   # Linux/Mac


Execute a aplicação:

python app.py


Acesse no navegador:

http://127.0.0.1:5000/

Próximos passos

Melhorar a interface visual

Implementar histórico de mensagens

Realizar deploy em serviço de hospedagem compatível com Flask
