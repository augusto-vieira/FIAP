# Classe de  Abstração que será herdada pelas demais.
class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, diaria: float):
        self.__marca = marca  # Atributo que armazena a marca do carro
        self.__modelo = modelo  # Atributo que armazena o modelo do carro
        self.__ano = ano  # Atributo que armazena o ano de fabricação do carro
        self.__diaria = diaria  # Atributo que armazena o preço diário de aluguel do carro
        self.__disponivel = True  # Atributo que indica se o carro está disponível para aluguel

    # Métodos Getters e Setters
    @property
    def marca(self) -> str:
        return self.__marca
    @marca.setter
    def marca(self, marca: str):
        self.__marca = marca

    @property
    def modelo(self) -> str:
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo: str):
        self.__modelo = modelo

    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def diaria(self) -> float:
        return self.__diaria
    
    @ano.setter
    def diaria(self, diaria: int):
        self.__ano = diaria

    @property
    def disponivel(self) -> bool:
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel: bool):
        self.__marca = disponivel
    
    # Métodos da Classe
    def informacao(self) -> str:
        return f"Marca: {self.__marca}, modelo: {self.__modelo}, Ano: {self.__ano}, Preço por dia: R${self.__diaria}"

    def verificar_disponibilidade(self) -> bool:
        return self.__disponivel

    def aluguel(self) -> str:
        if self.__disponivel:
            self.__disponivel = False
            return f"{self.__marca} {self.__modelo} foi alugado com sucesso!"
        else:
            return f"{self.__marca} {self.__modelo} não está disponível."

    def devolucao(self) -> str:
        self.__disponivel = True
        return f"{self.__marca} {self.__modelo} foi devolvido com sucesso!"
