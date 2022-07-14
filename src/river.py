class River:
    def __init__(self, name, num_fish):
        self.name = name
        self.num_fish = num_fish

    def river_name(self):
        return self.name

    def fish_count(self):
        return len(self.num_fish)

    def give_fish(self):
        return self.num_fish.pop()