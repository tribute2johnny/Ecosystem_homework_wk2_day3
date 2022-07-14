class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def bear_name(self):
        return self.name

    def eat_fish(self, fish_eaten):
        self.stomach.append(fish_eaten)

    def food_count(self):
        return len(self.stomach)

    
        
    def get_fish_from_river(self, river):
        fish = river.give_fish()
        self.eat_fish(fish)