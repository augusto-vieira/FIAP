# Classe de  Abstração que será herdada pelas demais.
class Veiculo:
    def __init__(self, marca, modelo, ano, diaria):
        self.__marca = marca  # Atributo que armazena a marca do carro
        self.__modelo = modelo  # Atributo que armazena o modelo do carro
        self.__ano = ano  # Atributo que armazena o ano de fabricação do carro
        self.__diaria = diaria  # Atributo que armazena o preço diário de aluguel do carro
        self.__disponivel = True  # Atributo que indica se o carro está disponível para aluguel

    def informacao(self):
        return f"Marca: {self.__marca}, modelo: {self.__modelo}, Ano: {self.__ano}, Preço por dia: R${self.__diaria}"

    def verificar_disponibilidade(self):
        return self.__disponivel

    def aluguel(self):
        if self.__disponivel:
            self.__disponivel = False
            return f"{self.__marca} {self.__modelo} foi alugado com sucesso!"
        else:
            return f"{self.__marca} {self.__modelo} não está disponível."

    def devolucao(self):
        self.__disponivel = True
        return f"{self.__marca} {self.__modelo} foi devolvido com sucesso!"
