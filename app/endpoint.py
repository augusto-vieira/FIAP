from utils.veiculo.carro import Carro              # Importa a classe Carro do módulo veiculo.carro
from utils.veiculo.motocicleta import Motocicleta  # Importa a classe Motocicleta do módulo veiculo.motocicleta
from utils.veiculo.caminhao import Caminhao        # Importa a classe Caminhao do módulo veiculo.caminhao
from utils.empresa.locadora import Locadora 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # Usado para criar classes de modelos de dados com validação automática e conversão de tipos.
from typing import List        # Usado para indicar que um campo ou variável deve conter uma lista de itens de um tipo específico.

app = FastAPI()

# Definindo modelos de dados usando Pydantic
class Veiculo(BaseModel):
    marca: str
    modelo: str
    ano: int
    preco_por_dia: float

class Carro(Veiculo):
    portas: int

class Motocicleta(Veiculo):
    cilindradas: int

class Caminhao(Veiculo):
    capacidade_carga: int

class Locadora(BaseModel):
    nome: str
    cnpj: str
    veiculos: List[Veiculo] = []

# Criando instâncias dos veículos
carro = Carro(marca="BMW", modelo="X1", ano=2020, preco_por_dia=150.00, portas=4)
moto = Motocicleta(marca="Suzuki", modelo="GSX-R1000", ano=2019, preco_por_dia=200.00, cilindradas=1000)
caminhao = Caminhao(marca="Mercedes-Benz", modelo="Actros", ano=2021, preco_por_dia=300.50, capacidade_carga=25000)

# Criando instância da locadora
locadora = Locadora(nome="Localiza Rent a Car Sa.", cnpj="16.670.085/0001-55", veiculos=[carro, moto, caminhao])

# Endpoint para obter as informações da locadora
@app.get("/locadora", response_model=Locadora)
def get_locadora():
    return locadora

# Endpoint para obter a lista de veículos
@app.get("/veiculos", response_model=List[Veiculo])
def get_veiculos():
    return locadora.veiculos

# Endpoint para obter um veículo específico pelo modelo
@app.get("/veiculos/{modelo}", response_model=Veiculo)
def get_veiculo(modelo: str):
    for veiculo in locadora.veiculos:
        if veiculo.modelo == modelo:
            return veiculo
        raise HTTPException(status_code=404, detail="Veículo não encontrado")