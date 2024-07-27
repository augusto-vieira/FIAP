from empresa.empresa import Empresa

# Implementa a Inteface <Empresa>
class Locadora(Empresa):
    def __init__(self, razao_social, cnpj):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__list = []
    
    # Implementando o método da Inteface <Empresa>
    def set_razao_social(self, razao_social, cnpj):
        self.__razao_social = razao_social
        self.__cnpj = cnpj

    def get_empresa(self):
        print(f"Empresa: {self.__razao_social} - CNPJ:{self.__cnpj}")

    # Implementando o método específico da Locadora
    def set_veiculo(self, veiculo):
        self.__list.append(veiculo)
    
    def get_veiculo(self):
        for Veiculo in self.__list:
            print(Veiculo.informacao())