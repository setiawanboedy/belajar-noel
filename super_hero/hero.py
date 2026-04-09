
# With health points attribute and method to count health points

class Hero:
    def __init__(self, name, power, health_points=100):
        self.name = name
        self.power = power
        self.health_points = health_points

    def use_power(self):
        return f"{self.name} uses {self.power}!"
    
    # fighter method
    def fight(self, opponent):
        if self.health_points > opponent.health_points:
            return f"{self.name} wins the fight against {opponent.name}!"
        elif self.health_points < opponent.health_points:
            return f"{opponent.name} wins the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {opponent.name} is a draw!"
    
    # Health method count health points
    def health(self):
        return f"{self.name} has {self.health_points} health points."
