from trust_basics import trust_result
import copy

DET_PLAY_BOOK = [1, 0, 1, 1]

class Character():

    changing_strategies = [
        'copycat',
        'grudger',
        'detective'
    ]


    def __init__(self, strategy, action=None, start_score=0):

        self.strategy = strategy
        self.score = start_score
        self.play_tally = []
        self.action = action
        self.player_id = None
        if self.strategy == 'detective':
            self.det_play_book = iter(DET_PLAY_BOOK)


    def play(self):
        if self.strategy in self.changing_strategies:
            self.action = self.get_action()
        return self.action

    def round(self, other):
        self_action = self.play()
        other_action = other.play()
        results = trust_result(self_action, other_action)

        self.play_tally.append(other_action)
        other.play_tally.append(self_action)

        self.score += results[0]
        other.score += results[1]

        return self_action, other_action

    def get_action(self):
        if self.strategy == 'copycat':
            if self.play_tally == []:
                # print(self.play_tally)
                return 1
            else:
                return self.play_tally[-1]
        if self.strategy == 'grudger':
            if 0 not in self.play_tally:
                return 1
            else:
                return 0
        if self.strategy == 'detective':
            try:
                return next(self.det_play_book)
            except StopIteration:
                if 0 not in self.play_tally:
                    return 0
                else:
                    return self.play_tally[-1]

    def reset(self):
        self.play_tally = []
        if self.strategy == 'detective':
            self.det_play_book = iter(DET_PLAY_BOOK)


if __name__ == '__main__':

    type_A = Character('cheat', action=0)
    type_B = Character('cooperate', action=1)
    type_C = Character('copycat')
    type_D = Character('grudger')
    type_E = Character('detective')

    # action_tally = []
    # score1_tally = []
    # score2_tally = []
    print(type_A.strategy, type_B.strategy)
    for i in range(10):
        type_A.round(type_B)
        print(type_A.score, type_B.score)

    type_A.reset()
    type_B.reset()

    print(type_A.strategy, type_C.strategy)

    for i in range(10):
        type_A.round(type_C)
        print(type_A.score, type_C.score)

    print(type_B.strategy, type_C.strategy)
    type_B.reset()
    type_C.reset()

    for i in range(10):
        type_B.round(type_C)
        print(type_B.score, type_C.score)
    type_C.reset()
    type_B.reset()
    # print(list(zip(action_tally, type_A.play_tally)))
    # print(list(zip(score1_tally, score2_tally)))
    # print(type_A.score)
    # print(type_B.score)
