import unittest
from src.river import River

class TestRiver(unittest.TestCase):
    
    def setUp(self):
        self.river("Clyde", 100)

    def test_river_has_name(self):
        self.assertEqual("Clyde", self.river.name)