from super_hero.hero import Hero

class Superman(Hero):
    def __init__(self, name, power, flight_speed, health_points=100):
        super().__init__(name, power, health_points)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies at a speed of {self.flight_speed}!"

    def health(self):
        return f"{self.name} has {self.health_points} health points."