# veiculos/moto.py
#from veiculo.veiculo import Veiculo
from veiculo_de_aluguel.veiculo.veiculo import Veiculo

# Herança: <Motocicleta> hedar os atributos e métodos de <Veiculo>
class Motocicleta(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, diaria: float, cilindrada):
        super().__init__(marca, modelo, ano, diaria)
        self.__cilindrada = cilindrada  # Cilindradas da motocicleta em cc

    @property
    def cilindrada(self) -> None:
        return self.__cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada: int):
        if not isinstance(cilindrada, int):
            raise TypeError("O valor da cilindrada deve ser um número inteiro")
        self.__cilindrada = cilindrada

    def informacao(self) -> str:
        base_info = super().informacao()  # Chama o método informacao da classe base
        return f"{base_info}, cilindrada: {self.__cilindrada}cc"  # Retorna a informações da classe base e cilindrada
