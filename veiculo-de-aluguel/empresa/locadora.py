from empresa.empresa import Empresa

# Implementa a Inteface <Empresa>
class Locadora(Empresa):
    def __init__(self):
        self._list = []
    
    # Implementando o método da Inteface <Empresa>
    def set_veiculo(self, veiculo):
        self._list.append(veiculo)
    
    def get_veiculo(self):
        for Veiculo in self._list:
            print(Veiculo.informacao())