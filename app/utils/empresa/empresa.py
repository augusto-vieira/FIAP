from abc import ABC, abstractmethod

#  Inteface: É uma Classe que só tem métodos abstratos 
class Empresa(ABC):

     # Método abstrato, deve ser implementado no objeto que herdar <Locadora>
    @abstractmethod
    def set_razao_social(self, razao_social: str):
        pass

    @abstractmethod
    def get_razao_social(self) -> str:
        pass

    @abstractmethod
    def set_cnpj(self, cnpj: str):
        pass

    @abstractmethod
    def get_cnpj(self) -> str:
        pass
    
    @abstractmethod
    def get_empresa(self) -> str:
        pass
