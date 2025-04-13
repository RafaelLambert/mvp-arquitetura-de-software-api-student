# 🧑‍🎓API Student - MVP Back-end - PUC-Rio

Este repositório contém o microsserviço de **gestão de estudantes** do projeto MVP proposto pela PUC-Rio. O serviço foi desenvolvido em Python utilizando o framework Flask, com SQLAlchemy para a modelagem do banco de dados e Pydantic para validação de dados.

Ele fornece uma API REST documentada com Swagger para cadastro, consulta, atualização e exclusão de estudantes, além de geração automática de matrícula.

---

## ⚙️Funcionalidades Principais

* **Cadastro de Estudantes:** Registra alunos com dados como nome, CPF, série, CEP e endereço.
* **Consulta por Nome:** Permite buscar um estudante pelo nome.
* **Consulta por CPF:** Permite buscar um estudante pelo CPF.
* **Listagem de Estudantes:** Retorna todos os estudantes cadastrados.
* **Atualização de Endereço:** Atualiza o endereço e CEP de um estudante.
* **Remoção de Estudantes:** Exclui um estudante com base em seu `id`.
* **Geração de Matrícula Única:** Cria uma matrícula no formato `M.AAAA.SS.XXX`, onde `SS` é a série e `XXX` o número sequencial.

---

## 🛠️Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask
* **Validação:** Pydantic
* **ORM:** SQLAlchemy
* **Extensões:** Flask-CORS, flask-openapi3
* **Documentação:** Swagger (via flask-openapi3)
* **Banco de Dados:** SQLite (padrão), com suporte a outros via SQLAlchemy
* **Testes:** nose2
* **Tipagem:** typing_extensions

---

## 🌐Endpoints da API

### 📄 Documentação

* **Rota:** `/`
* **Método:** GET
* **Descrição:** Redireciona para a interface de documentação Swagger/OpenAPI.

---

### 🧑‍🎓 Cadastro de Estudante

* **Rota:** `/student`
* **Método:** POST
* **Descrição:** Adiciona um novo estudante.
* **Body Exemplo:**

```json
{
  "name": "Rafael Marçal",
  "cpf": "12345678900",
  "grade_level": "1st grade",
  "cep": "00111222",
  "address": "Rua Exemplo 00"
}
```

---

### 📋 Listagem de Estudantes

* **Rota:** `/students`
* **Método:** GET
* **Descrição:** Lista todos os estudantes cadastrados.

---

### 🔎 Busca por Nome

* **Rota:** `/student`
* **Método:** GET
* **Query Param:** `name=NomeDoAluno`
* **Descrição:** Retorna os dados de um estudante com base no nome.

---

### 🔍 Busca por CPF

* **Rota:** `/student/cpf`
* **Método:** POST
* **Descrição:** Retorna os dados de um estudante com base no CPF.
* **Body Exemplo:**

```json
{
  "cpf": "12345678900"
}
```

---

### ✏️ Atualização de Endereço

* **Rota:** `/student`
* **Método:** PUT
* **Query Param:** `name=NomeDoAluno`
* **Body Exemplo:**

```json
{
  "cep": "98765432",
  "address": "Rua Atualizada, 123"
}
```

---

### 🗑️ Remoção de Estudante

* **Rota:** `/student`
* **Método:** DELETE
* **Query Param:** `id=IDdoAluno`
* **Descrição:** Remove o estudante com o ID informado.

---

## 🚀Como Executar o Projeto

### Executando Localmente com Virtual Enviroment

#### Pré-requisitos:

* Python 3.10+
* pip (gerenciador de pacotes)
* (Opcional) Ambiente virtual

#### Passos:

1. Clone este repositório:

```bash
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-student.git
cd mvp-arquitetura-de-software-api-student.git
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

A aplicação estará disponível em: [http://localhost:5001](http://localhost:5001)
A documentação Swagger estará disponível em: [http://localhost:5001/openapi](http://localhost:5001/openapi)

---

### 🐳Executando via Dockerfile

#### Pré-requisitos:

* Docker
* Docker Compose
* WSL2 (para usuários Windows)

#### Passos:

1. Clone este repositório:

   ```
   git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-student.git
   cd mvp-arquitetura-de-software-api-student.git
   ```
2. Abra o um terminal no diretório onde está o arquivo Dockerfile  e abra a distro Linux padrão:

   ```
   wsl
   ```
3. Construir Imagem Docker:

   ```
   docker build -t nome-da-imagem .
   ```
4. Verificar se a imagem foi criada:

   ```
   docker images
   ```
5. Rodar o container a partir da imagem:

   ```
   docker run -d -p 5000:5000 --name nome-do-container nome-da-imagem
   ```
6. Listar containers em execução:

   ```
   docker ps
   ```
7. A aplicação será inicializada no seguinte endereço:

   * **API Student:** [http://localhost:5001](http://localhost:5001)
   * **Documentação Swagger:** [http://localhost:5001/openapi](http://localhost:5001/openapi)

---

### 🐳 Executando com Docker Compose

#### Pré-requisitos:

* Docker
* Docker Compose (no serviço de Gateway))
* WSL2 (para usuários Windows)

#### Passos:

1. Clone este e os demais repositótios que compõe o sistema de microserviços:

   ```
   1. git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-escola-front.git
   2. git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-gateway.git
   3. git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-auth.git
   4. git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-grade.git
   5. git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-student.git
   ```
2. Certifique-se de que o `docker-compose.yml` esta dentro do projeto *mvp-arquitetura-de-software-api-gatewa*y.
3. No diretório do projeto *mvp-arquitetura-de-software-api-gatewa*y está o arquivo `docker-compose.yml`, execute:

```bash
docker-compose up --build
```

3. A aplicação será inicializada no seguinte endereço:

* **API Student:** [http://localhost:5001](http://localhost:5001)
* **Documentação Swagger:** [http://localhost:5001/openapi](http://localhost:5001/openapi)

## 📄Licença

Este projeto foi desenvolvido como parte de um MVP para a PUC-Rio e é destinado exclusivamente a fins educacionais.
