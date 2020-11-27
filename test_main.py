"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from math import pi
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_0(self):
        """Função que testa com 0."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            mock_input.assert_called()
            result = pi * float(input_returns[0])**2
            result = f'A área do círculo é {result:.2f}.'
            mock_print.assert_called_with(result)


    def test_10(self):
        """Função que testa com 10."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['10']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            mock_input.assert_called()
            result = pi * float(input_returns[0])**2
            result = f'A área do círculo é {result:.2f}.'
            mock_print.assert_called_with(result)

    def test_50(self):
        """Função que testa com 50."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['50']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            mock_input.assert_called()
            result = pi * float(input_returns[0])**2
            result = f'A área do círculo é {result:.2f}.'
            mock_print.assert_called_with(result)


    def test_1(self):
        """Função que testa com 1."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            mock_input.assert_called()
            result = pi * float(input_returns[0])**2
            result = f'A área do círculo é {result:.2f}.'
            mock_print.assert_called_with(result)

if __name__ == '__main__':
    unittest.main()
