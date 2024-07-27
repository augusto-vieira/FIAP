from abc import ABC, abstractmethod

#  Inteface: É uma Classe que só tem métodos abstratos 
class Empresa(ABC):

     # Método abstrato, deve ser implementado no objeto que herdar <Locadora>
    @abstractmethod
    def set_veiculo(self, veiculo):
        pass
    
    @abstractmethod
    def get_veiculo(self,):
        pass
