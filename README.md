# Criação do Sistema de Aluguel de Veículos

## Descrição
Desenvolver um sistema de aluguel de veículos utilizando os conceitos de Programação Orientada a Objetos (POO), FastAPI para a criação da API, Pytest para testes, Docker para containerização e UML para modelagem.

## Tarefas

### 1. Estruturação do Projeto
- 📝 Criar um repositório no GitHub.
- 📝 Configurar o ambiente de desenvolvimento.

### 2. Implementação das Classes (POO)
- 📝 Criar a classe `Vehicle` com os atributos protegidos e métodos públicos.
- 📝 Criar as subclasses `Car`, `Motorcycle` e `Truck` que herdam de `Vehicle`.
- 📝 Implementar o método `display_info` de forma polimórfica em cada subclasse.

### 3. Desenvolvimento da API com FastAPI
- 📝 Configurar o FastAPI no projeto.
- 📝 Criar endpoints para listar veículos, verificar disponibilidade, alugar e devolver veículos.
    - ⛳ GET `/vehicles` - Lista todos os veículos.
    - ⛳ GET `/vehicles/{vehicle_id}` - Mostra detalhes de um veículo específico.
    - ⛳ POST `/rent` - Aluga um veículo.
    - ⛳ POST `/return` - Devolve um veículo.

### 4. Testes com Pytest
- 📝 Escrever testes unitários para as classes `Vehicle`, `Car`, `Motorcycle` e `Truck`.
- 📝 Escrever testes para os endpoints da API.

### 5. Containerização com Docker
- 📝 Criar um `Dockerfile` para o projeto.
- 📝 Configurar o `docker-compose` para facilitar a execução do ambiente de desenvolvimento e testes.

### 6. Modelagem UML
- 📝 Criar diagramas de classe para representar a estrutura do sistema.
- 📝 Incluir diagramas de sequência para ilustrar o fluxo de operações principais.

## Critérios de Aceitação
- ✅ O sistema deve ser capaz de cadastrar, listar, alugar e devolver veículos.
- ✅ Todos os testes devem passar com sucesso.
- ✅ A aplicação deve rodar em um ambiente Docker configurado corretamente.
- ✅ A documentação deve incluir diagramas UML e instruções claras de uso e execução do sistema.

## Observações
- ⚠️ Utilize boas práticas de programação e versionamento de código.
- ⚠️ Faça commits frequentes e detalhados.
- ⚠️ Garanta que o código esteja bem documentado.

## Ambiente:
1. Criando um ambiente virtual:
```bash
python -m venv venv 
``` 
2. Ativando ambiente virtual:
```bash
venv\Scripts\activate
```
3. Instalando requirements
```bash
pip install -r requirements.txt 
```

## Ativando o Servidor Web
3. Instalando requirements
```bash
uvicorn main:app --reload
```

## Comandos utils
```bash
# Verificar o Caminho do Python
Get-Command python

# Verificar pacotes instalados
pip list

# Reinstalar os Pacotes 
pip install --upgrade --force-reinstall fastapi selenium
```