from veiculo_de_aluguel.veiculo.veiculo  import Veiculo

# Herança: <Caminhao> hedar os atributos e métodos de <Veiculo>
class Caminhao(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, diaria: float, capacidade_de_carga: int):
        super().__init__(marca, modelo, ano, diaria)
        self.__carga = None                 # Capacidade de carga em quilogramas
        self.carga = capacidade_de_carga    # Validar as informações, antes de atribuir na instanciação do objeto
    @property
    def carga(self) -> None:
        return self.__carga
    
    @carga.setter
    def carga(self, capacidade_de_carga: int):
        if not isinstance(capacidade_de_carga, int):
            raise TypeError("O valor da carga deve ser um número inteiro")
        self.__carga = capacidade_de_carga

    def informacao(self) -> str:
        base_info = super().informacao()  # Obtém informações da classe pai
        return f"{base_info}, Capacidade de carga: {self.__carga}kg"  # Retorna informações completas com a capacidade de carga
