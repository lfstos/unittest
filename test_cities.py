import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formated_name = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formated_name, 'Santiago, Chile - População 5000000')


if __name__ == '__main__':
    unittest.main()
