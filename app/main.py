class Animal:
    alive = []

    def __init__(self, name, health=100):
        self._health = health
        self.name = name
        self.hidden = False
        if self._health > 0:
            Animal.alive.append(self)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self):
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self):
        return self.__str__()


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        if not isinstance(animal, Herbivore):
            return

        if not animal.hidden:
            animal.health -= 50
