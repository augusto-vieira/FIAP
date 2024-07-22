from vehicles.vehicles import Vehicle

# Herança: <Car> hedar os atributos e métodos de <Vehicle>
class Car(Vehicle):
    def __init__(self, brand, model, year, daily_price, doors):
        super().__init__(brand, model, year, daily_price)
        self._doors = doors  # Atributo que armazena o número de portas do carro

    def display_info(self):
        base_info = super().display_info()  # Obtém as informações básicas da classe pai
        return f"{base_info}, Portas: {self._doors}"  # Adiciona o número de portas às informações

