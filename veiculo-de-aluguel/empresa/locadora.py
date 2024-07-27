from empresa.empresa import Empresa

# Implementa a Inteface <Empresa>
class Locadora(Empresa):
    def __init__(self):
        self.__list = []
    
    # Implementando o método da Inteface <Empresa>
    def set_veiculo(self, veiculo):
        self.__list.append(veiculo)
    
    def get_veiculo(self):
        for Veiculo in self.__list:
            print(Veiculo.informacao())