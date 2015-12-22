# Instruções de Uso

Este código foi desenvolvido com Python 2.7, para configurar seu uso basta utilizar a função `setup` do Makefile presente no diretório raiz do projeto da seguinte forma:

`$ make setup`

Esse comando configura o virtualenv para o projeto rodar, instalando as dependências listadas do arquivo requirements.txt

A configuração de rotas utiliza o microframework Flask e as interações com banco de dados (sqlite nesse caso) utiliza a ORM SQLAlchemy.

Para executar o servidor do site deve-se utilizar a função `run` do Makefile:

`$ make run`

Ao executar esse comando o projeto estará disponível através do endereço `http://localhost:5000`.
