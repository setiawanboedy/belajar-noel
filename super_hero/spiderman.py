from super_hero.hero import Hero

class Spiderman(Hero):
    def __init__(self, name, power, web_shooters, health_points=100):
        super().__init__(name, power, health_points)
        self.web_shooters = web_shooters

    def swing(self):
        return f"{self.name} swings through the city using {self.web_shooters}!"

    def health(self):
        return f"{self.name} has {self.health_points} health points."