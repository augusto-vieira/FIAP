## 💻 Instalação

Para configurar o ambiente de desenvolvimento e instalar todas as dependências necessárias, siga os passos abaixo:

1. 🐑 Clone este repositório:

    ```bash
    git clone https://github.com/augusto-vieira/atividade-POO.git
    ```
2. 📁 Entre no diretório do projeto:

    ```bash
    cd atividade-POO/
    ```

3. 🚩 Crie e ative um ambiente virtual:
    - Criando o ambiente.    
        ```bash
        python -m venv venv
        ```
    - Ativando no Linux.      
        ```bash
        source venv/bin/activate  
        ```
    - 💩 Ativando no Windowns.
        ```bash
        venv\Scripts\activate     
        ```        

4. 🚩 Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```
5. 📁 Entre no diretório app:
    ```bash
    cd ./app
    ``` 
## 🏹 Uso

Para executar o FastAPI, utilize o seguinte comando dentro do seu ambiente virtual:

```bash
uvicorn endpoint:app --reload
```

🔌 Certifique-se de estar na pasta correta ao executar o comando. Após iniciar, você verá uma mensagem de sucesso e poderá acessar a documentação da API em:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📋 Consultas Disponíveis

### 🎯 Locadora
Retorna os dados da locadora e seus veículos.

### 🎯Veículo
Retorna os dados do veículos.

### 🎯Veículo {modelo}
Retorna os dados do veículos pelo modelo.
