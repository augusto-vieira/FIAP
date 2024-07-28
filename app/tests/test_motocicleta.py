import pytest
from utils.veiculo.motocicleta import Motocicleta  

class TestMotocicleta:
    # Função de configuração do pytest para criar um objeto caminhão antes de cada teste 
    @pytest.fixture
    def motocicleta(self):
        return Motocicleta("Suzuki", "GSX-R1000", 2019, 200.90, 1000)
    
    def test_get_set_valor_da_cilindrada(self, motocicleta):
        """Teste para verificar a propriedade 'cilindrada' da Moto"""
        assert motocicleta.cilindrada == 1000  # Verifica o valor da cilindrada
        motocicleta.cilindrada = 250  # Altera o valor da cilindrada
        assert motocicleta.cilindrada == 250  # Verifica o valor da cilindrada