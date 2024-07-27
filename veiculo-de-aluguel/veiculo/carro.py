from veiculo.veiculo import Veiculo

# Herança: <Carro> hedar os atributos e métodos de <Veiculo>
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, diaria, portas):
        super().__init__(marca, modelo, ano, diaria)
        self.__portas = portas  # Atributo que armazena o número de portas do carro

    def informacao(self):
        base_info = super().informacao()  # Obtém as informações básicas da classe pai
        return f"{base_info}, Portas: {self.__portas}"  # Adiciona o número de portas às informações

