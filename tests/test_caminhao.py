import pytest
from veiculo_de_aluguel.veiculo.caminhao import Caminhao

class TestCaminhao:
    # Função de configuração do pytest para criar um objeto caminhão antes de cada teste 
    @pytest.fixture
    def caminhao(self):
        return Caminhao("Mercedes-Benz", "Actros", 2021, 300.50, 25000)
    
    def test_get_set_capacidade_de_carga(self, caminhao):
        """Teste para verificar a propriedade 'carga' do Caminhão"""
        assert caminhao.carga == 25000  # Verifica o valor da capacidade de carga
        caminhao.carga = 50000          # Altera o valor da capacidade de carga
        assert caminhao.carga == 50000  # Verifica o valor da capacidade de carga