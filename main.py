# main.py
from veiculo_de_aluguel.veiculo.carro import Carro              # Importa a classe Carro do módulo veiculo.carro
from veiculo_de_aluguel.veiculo.motocicleta import Motocicleta  # Importa a classe Motocicleta do módulo veiculo.motocicleta
from veiculo_de_aluguel.veiculo.caminhao import Caminhao        # Importa a classe Caminhao do módulo veiculo.caminhao
from veiculo_de_aluguel.empresa.locadora import Locadora        # Importa a classe Locadora do módulo empresa.locadora

def main():
    # Criando instâncias das classes de veículos
    carro = Carro("BMW", "X1", 2020, 150.00, 4)                          # Característica do Carro é 4 portas
    moto = Motocicleta("Suzuki", "GSX-R1000", 2019, 200.00, 1000)        # Característica da Motocicleta é 1000 cilindrada
    caminhao = Caminhao("Mercedes-Benz", "Actros", 2021, 300.50, 25000)  # Característica do Caminhao é de 25000kg de capacidade 

    # Colocamos todos os veículos em uma lista para simplificar a iteração
    veiculos = [carro, moto, caminhao]
    print(50 * "#")

    # Polimorfismos para apresentar as informações
    for veiculo in veiculos:
        print(veiculo.informacao())                 # Exibe as informações do veículo
        print(veiculo.aluguel())                    # Simula o aluguel do veículo
        print(veiculo.verificar_disponibilidade())  # Verifica a disponibilidade do veículo
        print(veiculo.devolucao())                  # Simula a devolução do veículo
        print(veiculo.verificar_disponibilidade())  # Verifica novamente a disponibilidade do veículo
        print()

    # Criando a locadora e adicionando veículos
    print(50 * "#")
    locadora = Locadora("Localiza Rent a Car Sa.", "16.670.085/0001-55")
    locadora.set_veiculo(carro)
    locadora.set_veiculo(moto)
    locadora.set_veiculo(caminhao)

    # Chamando o método da <empresa> implementado na <locadora>
    locadora.get_empresa()
   
    # Listando os veículos da locadora usando polimorfismo
    locadora.get_veiculo()
    print(50 * "#")

if __name__ == "__main__":
    main()  # Chama a função principal se este arquivo for executado diretamente
