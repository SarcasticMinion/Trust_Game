from characters import Character
import pandas as pd
import itertools
import random
import copy

class Game():

    player_count = 0

    def __init__(self, rounds, epochs=None):
        self.players = []
        self.rounds = rounds
        self.epochs = epochs

    def populate(self, player, number):
        for i in range(number):
            player.player_id = str(self.player_count).zfill(3)
            self.players.append(copy.deepcopy(player))
            self.player_count += 1
        random.shuffle(self.players)

    def simulate(self, round_by_round=False):
        for p1, p2 in itertools.combinations(self.players, 2):
            if round_by_round:
                print(p1.strategy, p2.strategy)

            for r in range(self.rounds):
                p1.round(p2)
                if round_by_round:
                    key_enter = input('')
            p1.reset()
            p2.reset()

    def winner(self):
        return max(self.players, key=lambda x: x.score)

    def tournament(self, epochs=None):
        if epochs:
            self.epochs = epochs

        for epoch in range(self.epochs):
            # print(epoch)
            self.simulate()
            self.players.sort(reverse=True, key=lambda x: x.score)
            del self.players[-5:]
            winners = copy.deepcopy(self.players[:5])
            for w in winners:
                w.player_id = str(self.player_count).zfill(3)
                self.player_count += 1
            self.players.extend(winners)
            for player in self.players:
                if epoch < self.epochs - 1:
                    player.born_again()
            # print(self)
            random.shuffle(self.players)

    def __repr__(self):
        self.players.sort(reverse=True, key=lambda x: x.score)
        league_table = pd.DataFrame([p.to_dict() for p in self.players])
        return str(league_table)


if __name__ == '__main__':
    type_A = Character('cheat', action=0)
    type_B = Character('cooperate', action=1)
    type_C = Character('copycat')
    # type_D = Character('grudger')
    # type_E = Character('detective')

    new_sim = Game(10, 3)
    new_sim.populate(type_A, 5)
    new_sim.populate(type_B, 15)
    new_sim.populate(type_C, 5)
    # new_sim.populate(type_D, 1)
    # new_sim.populate(type_E, 1)

    # new_sim.simulate(round_by_round=False)
    # print(new_sim.winner().strategy)
    new_sim.tournament()
    print(new_sim)
