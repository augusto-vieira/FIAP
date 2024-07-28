from veiculo_de_aluguel.empresa.empresa import Empresa
import re 

# Implementa a Inteface <Empresa>
class Locadora(Empresa):
    def __init__(self, razao_social: str, cnpj: str):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__list = []
    
    # Implementando o método da Inteface <Empresa>
    def set_razao_social(self, razao_social: str):
        if not isinstance(razao_social, str) and isinstance(cnpj, str):
            raise TypeError("A Razão social deve ser uma string ")    
        self.__razao_social = razao_social
    
    def get_razao_social(self) -> str:
        return self.__razao_social

    def set_cnpj(self, cnpj: str):
        if not isinstance(cnpj, str):
            raise TypeError("O CNPJ deve ser uma string")
         # Expressão regular para validar o formato "XX.XXX.XXX/0001-XX"
        formato = re.compile(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
        if formato.match(cnpj):           
            self.__cnpj = cnpj
        else:
            raise ValueError("Formato de CNPJ inválido! CNPJ: XX.XXX.XXX/0001-XX")

    def get_cnpj(self) -> str:
        return self.__cnpj

    def get_empresa(self) -> None:
        print(f"Empresa: {self.__razao_social} - CNPJ:{self.__cnpj}")

    # Implementando o método específico da Locadora
    def set_veiculo(self, veiculo):
        self.__list.append(veiculo)
    
    def get_veiculo(self) -> None:
        for Veiculo in self.__list:
            print(Veiculo.informacao())