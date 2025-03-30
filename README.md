# Intuitive Care Challenge

## Tasks:
- [x] WebScrapper, download de arquivos e compactação dos mesmos.
- [x] Vasculhar PDF e montar um CSV legível.
- [x] Ler arquivos, transformar e inserir em um Banco de Dados.
- [x] API + WebAPP.

## Tasks Path

1. **WebScrapper, Download e Zip**: [extract.py](./etl/extract.py)
2. **Vasculhar PDF e montar um CSV legível**: [transform.py](./etl/transform.py)
3. **Scripts SQL para criar tabelas, tratar dados e inserir**: [init.sql](./queries/init.sql), [populate_operadoras.sql](./queries/populate_operadoras.sql), [populate_demos_contabeis.sql](./queries/populate_demos_contabeis.sql)
4. **APP**:
- [API BackEnd](./app/main.py)
- [WebApp FrontEnd](./frontend/src/App.vue)

### Tecnologias

> **Python** com *Pandas* para Extração de Dados *(webScrapper ou leitura de arquivo)* e Transformação.
>
> **FastAPI** *(Python 3.13)* para Consulta dos Dados via **Requisições HTTP**.
>
>**VueJS** com *TypeScript e Vite* para o **WebApp**




### Como rodar o projeto com Container ?

1. Rode o arquivo docker-compose.yml
2. Serão criados 2 containers, um para a aplicação (API) e outro para o Banco de Dados MySQL


### Como rodar o projeto manualmente?

1. **Clone o repositório**:
   ```bash
    git clone https://github.com/seu-usuario/intuitive-care.git
    cd intuitive-care
   ```

2. **Configure o ambiente virtual**:
    - Certifique-se de ter o Python 3.13 instalado.

    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências do backend**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados**:
    - Certifique-se de que o banco de dados está configurado e rodando.
    - Atualize as configurações no arquivo .env (se necessário)

5. **Execute FastAPI**:
    ```bash
    uvicorn app.main:app --reload
    ```

6. **Instale as dependências do frontend**:
    - Certifique-se de ter o Node.js instalado.
    ```bash
    cd frontend
    npm install
    ```

7. **Execute o frontend (VueJS)**
    ```bash
    npm run dev
    ```

8. **Acesse o projeto**:
    - Backend: http://localhost:8000
    - Frontend: http://localhost:5173


### Como popular o banco de dados ?

1. Certifique-se que o banco de dados mysql esteja rodando local, docker ou cloud.
2. Execute os scripts **operacoes.py** e **demos_contabeis.py**
3. O banco de dados será populado concluindo assim a terceira tarefa.