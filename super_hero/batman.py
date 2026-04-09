from super_hero.hero import Hero

class Batman(Hero):
    def __init__(self, name, power, gadgets, health_points=100):
        super().__init__(name, power, health_points)
        self.gadgets = gadgets

    def use_gadgets(self):
        return f"{self.name} uses {', '.join(self.gadgets)}!"
    
    def health(self):
        return f"{self.name} has {self.health_points} health points."
    