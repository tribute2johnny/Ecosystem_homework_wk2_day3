import unittest
from src.bear import Bear
from src.fish import Fish
from src.river import River


class TestBear(unittest.TestCase):
    
    def setUp(self):
        self.bear = Bear("Rupert", "Brown bear")
        self.fish = Fish("Salmon")
        

    def test_bear_has_name(self):
        self.assertEqual("Rupert", self.bear.name)

    def test_bear_has_type(self):
        self.assertEqual("Brown bear", self.bear.type)

    def test_bear_food_count(self):
        self.assertEqual(0, self.bear.food_count())
        
    def test_bear_can_eat_fish(self):
        self.bear.eat_fish(self.fish)
        self.assertEqual(1, self.bear.food_count())

    # def test_bear_can_eat_fish(self):
    #     self.bear.eat_fish(self.fish)
    #     self.assertEqual(1, self.bear.food_count())
    #     self.assertEqual(99, self.river.remove_fish)
