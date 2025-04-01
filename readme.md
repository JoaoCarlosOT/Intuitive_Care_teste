
# TESTES DE NIVELAMENTO INTUITIVE CARE

Este projeto é composto por quatro testes que envolvem as seguintes áreas:

1. **Teste de Web Scraping**  
2. **Teste de Transformação de Dados**  
3. **Teste de Banco de Dados**  
4. **Teste de API**

Cada teste está organizado em um diretório específico dentro da pasta `INTUITIVE_CARE_TEST`. Abaixo estão as dependências necessárias para rodar o projeto e os requisitos de banco de dados.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

```
INTUITIVE_CARE_TEST/
│
├── Test_1/
├── Test_2/
├── Test_3/
└── Test_4/
```

## Dependências

### 1. Teste de Web Scraping
- **Python 3.x**  
  - **Bibliotecas necessárias:**
    - `requests` - para fazer requisições HTTP e baixar o conteúdo dos sites.
    - `beautifulsoup4` - para fazer o parsing do HTML e extrair os links para os arquivos PDF.
    - `pandas` - para manipular os dados extraídos, se necessário.
    - `zipfile` - para compactar os arquivos baixados em um arquivo ZIP.
  
  **Instalar dependências:**
  ```bash
  pip install requests beautifulsoup4 pandas
  ```

### 2. Teste de Transformação de Dados
- **Python 3.x**  
  - **Bibliotecas necessárias:**
    - `PyPDF2` ou `pdfplumber` - para extrair texto dos arquivos PDF.
    - `pandas` - para manipulação dos dados e conversão para CSV.
    - `zipfile` - para compactação do arquivo CSV.
  
  **Instalar dependências:**
  ```bash
  pip install pypdf2 pandas pdfplumber
  ```

### 3. Teste de Banco de Dados
- **Banco de Dados:**
  - **MySQL 8.0 ou PostgreSQL > 10.0**  
    Você precisará de um banco de dados MySQL ou PostgreSQL para importar os dados e executar as queries.

  **Dependências necessárias:**
  - Para MySQL:
    - `mysql-connector-python` ou `PyMySQL` - para conectar ao banco de dados MySQL.
  - Para PostgreSQL:
    - `psycopg2` - para conectar ao banco de dados PostgreSQL.

  **Instalar dependências:**
  ```bash
  pip install mysql-connector-python  # para MySQL
  pip install psycopg2  # para PostgreSQL
  ```

  Além disso, você deve baixar os arquivos CSV conforme descrito nas instruções do teste e configurar a conexão com o banco de dados para importar os dados.

### 4. Teste de API
- **Vue.js para front-end**  
  **Dependências necessárias:**
  - `axios` - para fazer requisições HTTP da interface para o servidor Python.
  
  **Instalar dependências do Vue.js:**
  ```bash
  npm install axios
  ```
  cd front-end
  npm install
  npm run dev

- **Python para back-end**  
  **Dependências necessárias:**
  - `Flask` ou `FastAPI` - para criar a API RESTful.
  - `pandas` - para manipular dados do CSV no back-end.
  
  **Instalar dependências do Python:**
  ```bash
  pip install flask pandas
  ```

### Banco utilizado:
- **MySQL 8.0** 

## Execução
OBS: Depois de baixar as dependencias de cada projeto e estar dentro do diretório correto, rode com o comando: python main.py

1. **Web Scraping**:  
   Navegue até o diretório `Test_1/` e execute o código para baixar os anexos e compactá-los.

2. **Transformação de Dados**:  
   Navegue até o diretório `Test_2/` e execute o código para extrair os dados dos PDFs e salvar em CSV.

3. **Banco de Dados**:  
   Navegue até o diretório `Test_3/` e execute os scripts SQL para importar os dados para o banco de dados e criar as queries analíticas.

4. **API**:  
   Navegue até o diretório `Test_4/` e execute o servidor Python para manipulação dos dados. Em seguida, execute a interface Vue.js para interagir com o servidor.

