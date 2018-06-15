import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Testa com nome, nome do meio e sobrenome."""
        formatted_name = get_formatted_name('luiz', 'dos santos', 'fernando')
        self.assertEqual(formatted_name, 'Luiz Fernando Dos Santos')


if __name__ == '__main__':
    unittest.main()
