from utils.veiculo.veiculo import Veiculo

# Herança: <Carro> hedar os atributos e métodos de <Veiculo>
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, diaria: float, portas:int):
        super().__init__(marca, modelo, ano, diaria)
        self.__portas = None   # Atributo que armazena o número de portas do carro
        self.portas = portas   # Durante a instanciação do objeto, ele vai validar o número de portas.

    @property
    def portas(self) -> None:
        return self.__portas

    @portas.setter
    def portas(self, portas: int):
        if not isinstance(portas, int):
            raise TypeError("A quantidade de portas deve ser um número inteiro")
        # Verifica a quantidade de portas
        if portas >= 1 and portas <= 5:
            self.__portas = portas
        else:
            raise ValueError("A quantidade de portas deve ser maior ou igual 1 e menor ou igual a 5")

    def informacao(self) -> str:
        base_info = super().informacao()  # Obtém as informações básicas da classe pai
        return f"{base_info}, Portas: {self.__portas}"  # Adiciona o número de portas às informações

