# main.py
from vehicles.car import Car  # Importa a classe Car do módulo vehicles.car
from vehicles.motorcycle import Motorcycle  # Importa a classe Motorcycle do módulo vehicles.motorcycle
from vehicles.truck import Truck  # Importa a classe Truck do módulo vehicles.truck
from company.rental_company import RentalCompany
def main():
    # Criando instâncias das classes de veículos
    carro = Car("BMW", "X1", 2020, 150, 4)  # Característica do Car é 4 portas
    moto = Motorcycle("Suzuki", "GSX-R1000", 2019, 200, 1000)  # Característica da Motorcycle é 1000 cilindrada
    caminhao = Truck("Mercedes-Benz", "Actros", 2021, 300, 25000)  # Característica Truck carga 25000kg capacitade 

    # Colocamos todos os veículos em uma lista para simplificar a iteração
    veiculos = [carro, moto, caminhao]

    # Polimorfismos para apresentar as informações
    for veiculo in veiculos:
        print(veiculo.display_info())  # Exibe as informações do veículo
        print(veiculo.rent())  # Simula o aluguel do veículo
        print(veiculo.check_availability())  # Verifica a disponibilidade do veículo
        print(veiculo.return_vehicle())  # Simula a devolução do veículo
        print(veiculo.check_availability())  # Verifica novamente a disponibilidade do veículo
        print()

    # Criando a locadora e adicionando veículos
    print(50 * "#")
    print("Locadora: ")
    locadora = RentalCompany()
    locadora.set_vehicles(carro)
    locadora.set_vehicles(moto)
    locadora.set_vehicles(caminhao)

    # Listando os veículos da locadora usando polimorfismo
    locadora.get_vehicles()
    print(50 * "#")
    
if __name__ == "__main__":
    main()  # Chama a função principal se este arquivo for executado diretamente
