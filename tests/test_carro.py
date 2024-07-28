import pytest
from veiculo_de_aluguel.veiculo.carro import Carro  

class TestCarro:
    # Função de configuração do pytest para criar um objeto caminhão antes de cada teste 
    @pytest.fixture
    def carro(self):
        return Carro("BMW", "X1", 2020, 150, 4)
    
    def test_get_set_quantidade_de_portas(self, carro):
        """Teste para verificar a propriedade 'porta' do Carro"""
        assert carro.portas == 4  # Verifica o valor da quantidade de porta
        carro.portas = 3  # Altera o valor da quantidade de porta
        assert carro.portas == 3  #  Verifica o valor da quantidade de porta

    def test_quando_numero_de_portas_for_invalido_deve_retornar_exception(self, carro):
        # Chamar a Exception do pytest
        with pytest.raises(Exception):
           # informar um número de portas inválido
           carro.portas = 10
           resultado = carro.portas
           assert resultado