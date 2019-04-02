import random


class Animal:
    def __init__(self, name):
        self.name = name

    def add_to_river(self, river):
        while True:
            point = random.randint(0, len(river) - 1)
            if river[point] is None:
                river[point] = eval(
                    self.__class__.__name__ + '("' + self.name + '")')
                break
        return river

    def change_position(self, river):
        select = random.randint(0, 2)
        position = river.index(self)
        if select == 0:
            try:
                river[position + 1]
            except IndexError:
                position = -1
            if river[position + 1] is None:
                river[position] = None
                river[position + 1] = self
            elif river[position + 1].name == self.name and None in river:
                upd_river = self.add_to_river(river)
                return upd_river
            elif river[position + 1].name == 'bear' and self.name == 'fish':
                river[position] = None
            elif river[position + 1].name == 'fish' and self.name == 'bear':
                river[position] = None
                river[position + 1] = self
            else:
                pass
        elif select == 1:
            river[position] = self
        elif select == 2:
            if river[position - 1] is None:
                river[position] = None
                river[position - 1] = self
            elif river[position - 1].name == self.name and None in river:
                upd_river = self.add_to_river(river)
                return upd_river
            elif river[position - 1].name == 'bear' and self.name == 'fish':
                river[position] = None
            elif river[position - 1].name == 'fish' and self.name == 'bear':
                river[position] = None
                river[position - 1] = self
            else:
                pass
        return river


class Bear(Animal):
    pass


class Fish(Animal):
    pass


class River:
    def __init__(self, animals, length):
        self.animals = animals
        self.ecosystem = [None for i in range(length)]

    def __str__(self):
        ecosystem_representation = [' ' for i in range(len(self.ecosystem))]
        for i in range(len(self.ecosystem)):
            try:
                if self.ecosystem[i].name == 'fish':
                    ecosystem_representation[i] = u'\U0001F41F'
                elif self.ecosystem[i].name == 'bear':
                    ecosystem_representation[i] = u'\U0001F43B'
            except AttributeError:
                ecosystem_representation[i] = u'\u301C'
        return ''.join(ecosystem_representation)

    def add_animal(self, animal, place):
        try:
            assert 0 <= place <= len(self.ecosystem) - 1
            assert self.ecosystem[place] is None
        except AssertionError:
            return None
        else:
            self.ecosystem[place] = animal

    def count_animals(self, name):
        counter = 0
        for i in self.ecosystem:
            try:
                if i.name == name:
                    counter += 1
                else:
                    continue
            except AttributeError:
                continue
        return counter

    def create_ecosystem(self):
        for i in range(len(self.ecosystem)):
            to_place = random.randint(0, 1)
            if to_place:
                if self.animals:
                    animal = random.choice(self.animals)
                    self.add_animal(animal, i)
                    self.animals.remove(animal)
                else:
                    break
        return self.ecosystem

    def update_ecosystem(self, steps=1):
        for i in range(steps):
            for animal in self.ecosystem:
                try:
                    self.ecosystem = animal.change_position(self.ecosystem)
                except AttributeError:
                    self.ecosystem = self.ecosystem
        return self