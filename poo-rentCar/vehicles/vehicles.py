# Classe de  Abstração que será herdada pelas demais.
class Vehicle:
    def __init__(self, brand, model, year, daily_price):
        self._brand = brand  # Atributo que armazena a marca do carro
        self._model = model  # Atributo que armazena o modelo do carro
        self._year = year  # Atributo que armazena o ano de fabricação do carro
        self._daily_price = daily_price  # Atributo que armazena o preço diário de aluguel do carro
        self._available = True  # Atributo que indica se o carro está disponível para aluguel

    def display_info(self):
        return f"Marca: {self._brand}, Modelo: {self._model}, Ano: {self._year}, Preço por dia: R${self._daily_price}"

    def check_availability(self):
        return self._available

    def rent(self):
        if self._available:
            self._available = False
            return f"{self._brand} {self._model} foi alugado com sucesso!"
        else:
            return f"{self._brand} {self._model} não está disponível."

    def return_vehicle(self):
        self._available = True
        return f"{self._brand} {self._model} foi devolvido com sucesso!"
