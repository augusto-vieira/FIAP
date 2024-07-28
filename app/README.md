# Criação do Sistema de Aluguel de Veículos

## Descrição
Desenvolver um sistema de aluguel de veículos utilizando os conceitos de Programação Orientada a Objetos (POO), FastAPI para a criação da API, Pytest para testes, Docker para containerização e UML para modelagem.

## Tarefas

### 1. Estruturação do Projeto
- 📝 Criar um repositório no GitHub.
- 📝 Configurar o ambiente de desenvolvimento.

### 2. Implementação das Classes (POO)
- 📝 Criar a classe `Veiculo` com os atributos protegidos e métodos públicos.
- 📝 Criar as subclasses `Carro`, `Motocicleta` e `Caminhao` que herdam de `Veiculo`.
- 📝 Implementar o método `informacao` de forma polimórfica em cada subclasse.
- 📝 Criar a Interface `Empresa`, que será implementada na classe `Locadora`.
- 📝 Criar a classe`Locadora` e implementa a interface `Empresa`

### 3. Desenvolvimento da API com FastAPI
- 📝 Configurar o FastAPI no projeto.
- 📝 Criar endpoints para listar veículos, verificar disponibilidade, alugar e devolver veículos.
    - ⛳ GET `/locadora` - Lista a Locadora e seus veículos.
    - ⛳ GET `/veiculo` - Lista todos os veículos.
    - ⛳ GET `/veiculo/{modelo}` - Mostra detalhes de um veículo específico.

### 4. Testes com Pytest
- 📝 Escrever testes unitários para as classes `Veiculo`, `Carro`, `Motocicleta`, `Caminhao`, `Locadora`.

### 5. Modelagem UML
- 📝 Criar diagramas de classe para representar a estrutura do sistema.

## Critérios de Aceitação
- ✅ O sistema deve ser capaz de cadastrar, listar, alugar e devolver veículos.
- ✅ Todos os testes devem passar com sucesso.
- ✅ A aplicação deve rodar em um ambiente Docker configurado corretamente.
- ✅ A documentação deve incluir diagramas UML e instruções claras de uso e execução do sistema.

## Observações
- ⚠️ Utilize boas práticas de programação e versionamento de código.
- ⚠️ Faça commits frequentes e detalhados.
- ⚠️ Garanta que o código esteja bem documentado.