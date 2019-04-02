from ecosys import *


class Main:
    def __init__(self, river, cycles, bears, fish):
        self.cycles = eval(cycles)
        self.river = eval(river)
        self.bears = eval(bears)
        self.fish = eval(fish)

    def create_assets(self):
        bears = [Bear('bear') for i in range(self.bears)]
        fish = [Fish('fish') for i in range(self.fish)]
        animals = bears + fish
        ecosystem = River(animals, self.river)
        cycles = self.cycles
        return animals, ecosystem, cycles


def start():
    river = input('Enter the river size: ')
    repeats = input('Enter count of cycles: ')
    bears = input('... and amount of bears: ')
    fish = input('... and amount of fish: ')
    print('>>>Let\'s start the game!<<<\n')
    return river, repeats, bears, fish


def run():
    while True:
        try:
            user_input = start()
            main = Main(*user_input)
        except AssertionError:
            print('Wrong data. Try again')
        else:
            break
    animals, ecosystem, cycles = main.create_assets()
    ecosystem.create_ecosystem()
    for i in range(cycles):
        new_ecosystem = ecosystem.update_ecosystem()
        riv = '>>>[{} bears vs. {} fish]'.format(
            new_ecosystem.count_animals('bear'),
            new_ecosystem.count_animals('fish'))
        print('-' * 2 * len(new_ecosystem.__str__()))
        print(new_ecosystem, riv)
        print('-' * 2 * len(new_ecosystem.__str__()))


if __name__ == '__main__':
    run()
