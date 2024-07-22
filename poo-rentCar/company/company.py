from abc import ABC, abstractmethod

#  Inteface: É uma Classe que só tem métodos abstratos 
class Company(ABC):

     # Método abstrato, deve ser implementado no objeto que herdar <RentalCompany>
    @abstractmethod
    def set_vehicles(self, vehicles):
        pass
    
    @abstractmethod
    def get_vehicles(self,):
        pass
