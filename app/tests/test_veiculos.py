import pytest                        # Importar funções do pytest
from pytest import mark              # <mark> usado para utlizar os decorator nos testes específicos
from veiculo_de_aluguel.veiculo.veiculo import Veiculo

class TestVeiculo:
   # Função de configuração do pytest para criar um objeto veiculo antes de cada teste 
    @pytest.fixture
    def veiculo(self):
        return Veiculo("Fiat", "Uno", 2020, 150.0)

    # Teste para verificar o getter e setter da marca
    @mark.metodos_veiculo
    def test_get_set_marca(self, veiculo):
        """Teste para verificar a propriedade 'marca' do veículo"""
        assert veiculo.marca == "Fiat"  # Verifica o valor inicial da marca
        veiculo.marca = "Ford"  # Altera o valor da marca
        assert veiculo.marca == "Ford"  # Verifica o novo valor da marca

    # Teste para verificar o getter e setter do modelo
    @mark.metodos_veiculo
    def test_get_set_modelo(self, veiculo):
        """Teste para verificar a propriedade 'modelo' do veículo"""
        assert veiculo.modelo == "Uno"  # Verifica o valor inicial do modelo
        veiculo.modelo = "Ka"  # Altera o valor do modelo
        assert veiculo.modelo == "Ka"  # Verifica o novo valor do modelo

    # Teste para verificar o getter e setter do ano
    @mark.metodos_veiculo
    def test_get_set_ano(self, veiculo):
        """Teste para verificar a propriedade 'ano' do veículo"""
        assert veiculo.ano == 2020  # Verifica o valor inicial do ano
        veiculo.ano = 2021  # Altera o valor do ano
        assert veiculo.ano == 2021  # Verifica o novo valor do ano

    # Teste para verificar o getter e setter da diaria
    @mark.metodos_veiculo
    def test_get_set_diaria(self, veiculo):
        """Teste para verificar a propriedade 'diaria' do veículo"""
        assert veiculo.diaria == 150.0  # Verifica o valor inicial da diaria
        veiculo.diaria = 200.0  # Altera o valor da diaria
        assert veiculo.diaria == 200.0  # Verifica o novo valor da diaria

    # Teste para verificar o getter e setter da disponibilidade
    @mark.metodos_veiculo  # decorator
    def test_get_set_disponivel(self, veiculo):
        """Teste para verificar a propriedade 'disponivel' do veículo"""
        assert veiculo.disponivel == True  # Verifica o valor inicial da disponibilidade
        veiculo.disponivel = False  # Altera o valor da disponibilidade
        assert veiculo.disponivel == False  # Verifica o novo valor da disponibilidade 