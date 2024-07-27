from abc import ABC, abstractmethod

#  Inteface: É uma Classe que só tem métodos abstratos 
class Empresa(ABC):

     # Método abstrato, deve ser implementado no objeto que herdar <Locadora>
    @abstractmethod
    def set_razao_social(self, razao_social, cnpj):
        pass
    
    @abstractmethod
    def get_empresa(self):
        pass
