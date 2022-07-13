import unittest
from src.fish import Fish
from src.bear import Bear


class TestFish(unittest.TestCase):

    def setUp(self):
        self.fish = Fish("Salmon")

    def test_fish_has_name(self):
        self.assertEqual("Salmon", self.fish.name)