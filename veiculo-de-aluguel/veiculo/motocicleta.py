# veiculos/moto.py
from veiculo.veiculo import Veiculo

# Herança: <Motocicleta> hedar os atributos e métodos de <Veiculo>
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, diaria, cilindrada):
        super().__init__(marca, modelo, ano, diaria)
        self._cilindrada = cilindrada  # Cilindradas da motocicleta em cc

    def informacao(self):
        base_info = super().informacao()  # Chama o método informacao da classe base
        return f"{base_info}, cilindrada: {self._cilindrada}cc"  # Retorna a informações da classe base e cilindrada
