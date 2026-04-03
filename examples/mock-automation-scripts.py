
import unittest
from unittest.mock import Mock, patch, MagicMock
import requests

class Service:
    def fetch_data(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Manage the HTTP errors
        return response.json()

class TestService(unittest.TestCase):
    
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        # """Test the nominal case with valid response"""
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {'chave': 'valor'}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Act
        service = Service()
        resultado = service.fetch_data('https://api.exemplo.com.br')
        
        # Assert
        self.assertEqual(resultado, {'chave': 'valor'})
        mock_get.assert_called_once_with('https://api.exemplo.com.br')
    
    @patch('requests.get')
    def test_fetch_data_http_error(self, mock_get):
        # """Test HTTP error handling"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Não Encontrado")
        mock_get.return_value = mock_response
        
        service = Service()
        with self.assertRaises(requests.HTTPError):
            service.fetch_data('https://api.exemplo.com.br/nao-encontrado')
    
    @patch('requests.get')
    def test_fetch_data_invalid_json(self, mock_get):
        # """Test with invalid JSON"""
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("JSON Inválido")
        mock_get.return_value = mock_response
        
        service = Service()
        with self.assertRaises(ValueError):
            service.fetch_data('https://api.exemplo.com.br')
    
    @patch('requests.get')
    def test_fetch_data_timeout(self, mock_get):
        # """Test connection timeout"""
        mock_get.side_effect = requests.Timeout("Tempo de conexão esgotado")
        
        service = Service()
        with self.assertRaises(requests.Timeout):
            service.fetch_data('https://api.exemplo.com.br')

if __name__ == '__main__':
    unittest.main()
