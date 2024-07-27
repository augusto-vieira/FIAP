# Classe de  Abstração que será herdada pelas demais.
class Veiculo:
    def __init__(self, marca, modelo, ano, diaria):
        self._marca = marca  # Atributo que armazena a marca do carro
        self._modelo = modelo  # Atributo que armazena o modelo do carro
        self._ano = ano  # Atributo que armazena o ano de fabricação do carro
        self._diaria = diaria  # Atributo que armazena o preço diário de aluguel do carro
        self._disponivel = True  # Atributo que indica se o carro está disponível para aluguel

    def informacao(self):
        return f"Marca: {self._marca}, modelo: {self._modelo}, Ano: {self._ano}, Preço por dia: R${self._diaria}"

    def verificar_disponibilidade(self):
        return self._disponivel

    def aluguel(self):
        if self._disponivel:
            self._disponivel = False
            return f"{self._marca} {self._modelo} foi alugado com sucesso!"
        else:
            return f"{self._marca} {self._modelo} não está disponível."

    def devolucao(self):
        self._disponivel = True
        return f"{self._marca} {self._modelo} foi devolvido com sucesso!"
