class Planet:
    def __init__(self, name="Def", population = None, weight):
        self.name = name
        self.population = population or []
        self._weight = weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"
    weight = property()
    @weight.setter
    def weight(self, kg):
        self._weight = kg

    @weight.getter
    def weight(self):
        return self._weight

    @weight.deleter
    def weight(self):
        print ("we are going to delete weight")
        del self._weight


#    @classmethod
#    @staticmethod
class Human:
    """my class"""

print (Human.__doc__)
print(dir(Planet))


earth = Planet("Earth", 10, 100)
print(earth)
print(earth.name)
solar_system = []
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for planet_name in planet_names:
    planet = Planet(planet_name)
    solar_system.append(planet)
    print(planet.__dict__)
print(solar_system)
print(solar_system[0].__getattribute__)


###########################

