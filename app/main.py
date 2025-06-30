class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.health = health
        self.name = name
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

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
            if animal.health <= 0:
                Animal.alive.remove(animal)