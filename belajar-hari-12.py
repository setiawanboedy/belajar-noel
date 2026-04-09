from super_hero.batman import Batman
from super_hero.superman import Superman
from super_hero.spiderman import Spiderman

if __name__ == "__main__":
    # Create instances of each hero
    spiderman = Spiderman("Peter Parker", "Spider-Sense", "Web Shooters", 80)
    batman = Batman("Bruce Wayne", "Intellect", ["Batarang", "Grappling Hook"], 100)
    superman = Superman("Clark Kent", "Super Strength", "Mach 10", 50)

    # Use their powers and abilities
    print(spiderman.use_power())
    print(spiderman.swing())
    print(batman.use_power())
    print(batman.use_gadgets())
    print(superman.use_power())
    print(superman.fly())

    # Simulate a fight between Spiderman and Batman
    print(spiderman.fight(batman))
    # Simulate a fight between Superman and Spiderman
    print(superman.fight(spiderman))
    # Simulate a fight between Batman and Superman
    print(batman.fight(superman))