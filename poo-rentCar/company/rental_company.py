from company.company import Company

# Implementa a Inteface <Company>
class RentalCompany(Company):
    def __init__(self):
        self._list = []
    
    # Implementando o método da Inteface <Company>
    def set_vehicles(self, vehicles):
        self._list.append(vehicles)
    
    def get_vehicles(self):
        for vehicle in self._list:
            print(vehicle.display_info())