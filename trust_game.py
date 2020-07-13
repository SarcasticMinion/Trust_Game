from characters import BaseCharacter
import itertools
import copy

class Game():

    def __init__(self, rounds):
        self.players = []
        self.rounds = rounds

    def populate(self, player, number):
        for i in range(number):
            self.players.append(copy.deepcopy(player))

    def simulate(self):
        for p1, p2 in itertools.combinations(self.players, 2):
            for r in range(self.rounds):
                p1.round(p2)

    def winner(self):
        return max(self.players, key=lambda x: x.score)


if __name__ == '__main__':
    type_A = BaseCharacter('cheat', action=0)
    type_B = BaseCharacter('cooperate', action=1)
    type_C = BaseCharacter('copycat')
    type_D = BaseCharacter('grudger', action=1)
    type_E = BaseCharacter('detective')

    new_sim = Game(10)
    new_sim.populate(type_A, 1)
    new_sim.populate(type_B, 1)
    new_sim.populate(type_C, 1)
    new_sim.populate(type_D, 1)
    new_sim.populate(type_B, 1)

    new_sim.simulate()
    print(new_sim.winner().strategy)
