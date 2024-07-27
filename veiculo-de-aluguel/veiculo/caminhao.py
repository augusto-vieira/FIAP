# veiculos/caminhao.py
from veiculo.veiculo import Veiculo

# Herança: <Caminhao> hedar os atributos e métodos de <Veiculo>
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, diaria, capacidade_de_carga):
        super().__init__(marca, modelo, ano, diaria)
        self.__carga = capacidade_de_carga  # Capacidade de carga em quilogramas

    def informacao(self):
        base_info = super().informacao()  # Obtém informações da classe pai
        return f"{base_info}, Capacidade de carga: {self.__carga}kg"  # Retorna informações completas com a capacidade de carga
