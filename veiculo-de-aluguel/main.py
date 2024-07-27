# main.py
from veiculo.carro import Carro  # Importa a classe Carro do módulo veiculo.carro
from veiculo.motocicleta import Motocicleta  # Importa a classe Motocicleta do módulo veiculo.motocicleta
from veiculo.caminhao import Caminhao  # Importa a classe Caminhao do módulo veiculo.caminhao
from empresa.locadora import Locadora

def main():
    # Criando instâncias das classes de veículos
    carro = Carro("BMW", "X1", 2020, 150, 4)  # Característica do Carro é 4 portas
    moto = Motocicleta("Suzuki", "GSX-R1000", 2019, 200, 1000)  # Característica da Motocicleta é 1000 cilindrada
    caminhao = Caminhao("Mercedes-Benz", "Actros", 2021, 300, 25000)  # Característica do Caminhao é de 25000kg de capacidade 

    # Colocamos todos os veículos em uma lista para simplificar a iteração
    veiculos = [carro, moto, caminhao]

    # Polimorfismos para apresentar as informações
    for veiculo in veiculos:
        print(veiculo.informacao())  # Exibe as informações do veículo
        print(veiculo.aluguel())  # Simula o aluguel do veículo
        print(veiculo.verificar_disponibilidade())  # Verifica a disponibilidade do veículo
        print(veiculo.devolucao())  # Simula a devolução do veículo
        print(veiculo.verificar_disponibilidade())  # Verifica novamente a disponibilidade do veículo
        print()

    # Criando a locadora e adicionando veículos
    print(50 * "#")
    print("Locadora: ")
    locadora = Locadora()
    locadora.set_veiculo(carro)
    locadora.set_veiculo(moto)
    locadora.set_veiculo(caminhao)

    # Listando os veículos da locadora usando polimorfismo
    locadora.get_veiculo()
    print(50 * "#")
    
if __name__ == "__main__":
    main()  # Chama a função principal se este arquivo for executado diretamente
