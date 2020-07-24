from characters import Character
import itertools
import copy

class Game():

    player_count = 0

    def __init__(self, rounds):
        self.players = []
        self.rounds = rounds

    def populate(self, player, number):
        for i in range(number):
            player.player_id = str(self.player_count).zfill(3)
            self.players.append(copy.deepcopy(player))
            self.player_count += 1

    def simulate(self, round_by_round=False):
        for p1, p2 in itertools.combinations(self.players, 2):
            if round_by_round:
                print(p1.strategy, p2.strategy)
            # print(p1.play_tally)
            # print(p1.play_tally)

            for r in range(self.rounds):
                p1.round(p2)
                if round_by_round:
                    # print(p1.score, p2.score)
                    key_enter = input('')
            p1.reset()
            p2.reset()

                # print(p1.player_id, p2.player_id)
    def census(self):
        for player in self.players:
            print(player.strategy)

    def winner(self):
        return max(self.players, key=lambda x: x.score)


if __name__ == '__main__':
    type_A = Character('cheat', action=0)
    type_B = Character('cooperate', action=1)
    type_C = Character('copycat')
    type_D = Character('grudger')
    type_E = Character('detective')

    new_sim = Game(10)
    new_sim.populate(type_A, 1)
    new_sim.populate(type_B, 1)
    new_sim.populate(type_C, 1)
    new_sim.populate(type_D, 1)
    new_sim.populate(type_E, 1)

    # new_sim.census()

    new_sim.simulate(round_by_round=False)
    print(new_sim.winner().strategy)
    # scores = [p.score for p in new_sim.players]
    # print(scores)
