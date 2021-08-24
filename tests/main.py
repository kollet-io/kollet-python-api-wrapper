import unittest
from kollet_io.kollet import Kollet

class TestKollet(unittest.TestCase):
    def __init__(self):
        self.client = Kollet("API_KEY")

    def test_get_currencies(self):
        currencies = self.client.get_currencies()
        self.assertTrue(currencies["success"])



if __name__ == '__main__':
    unittest.main()