import pytest
from utils.empresa.locadora import Locadora

class Testlocadora:
    # Função de configuração do pytest para criar um objeto caminhão antes de cada teste 
    @pytest.fixture
    def locadora(self):
        return Locadora("Localiza Rent a Car Sa.", "16.670.085/0001-55")
    
    def test_get_set_razao_social(self, locadora):
        """Teste para verificar a propriedade 'razao_social' da Locadora"""
        assert locadora.get_razao_social() == "Localiza Rent a Car Sa."  # Verifica o nome da Locadora
        locadora.set_razao_social("Webmotors S.A.")  # Altera o nome da Locadora
        assert locadora.get_razao_social() == "Webmotors S.A."  # Verifica o nome da Locadora

    def test_get_set_cnpj(self, locadora):
        """Teste para verificar a propriedade 'razao_social' da Locadora"""
        assert locadora.get_cnpj() == "16.670.085/0001-55"  # Verifica o CNPJ
        locadora.set_cnpj("03.347.828/0001-09")  # Altera o CNPJ
        assert locadora.get_cnpj() == "03.347.828/0001-09"  # Verifica o CNPJ  
    
    def test_quando_receber_cnpj_errado_retornar_exception(self, locadora):
        # Chamar a Exception do pytest
        with pytest.raises(Exception):
           # informar um cnpj inválido
           resultado = locadora.set_cnpj("01.234.567/0001-09111") 
           assert resultado