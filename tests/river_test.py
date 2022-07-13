import unittest
from src.river import River
from src.bear import Bear


class TestRiver(unittest.TestCase):
    
    def setUp(self):
        self.river = River("Clyde", 100)

    def test_river_has_name(self):
        self.assertEqual("Clyde", self.river.name)

    def test_amount_of_fish(self):
        self.assertEqual(100, self.river.num_fish)

    def test_remove_fish(self):
        self.assertEqual(99, self.river.remove_fish())