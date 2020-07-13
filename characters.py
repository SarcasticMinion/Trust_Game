from trust_basics import trust_result

class BaseCharacter():

    changing_strategies = [
        'copycat',
        'grudger',
        'detective'
    ]
    det_play_book = iter([
        1, 0, 1, 1
    ])

    def __init__(self, strategy, action=None, start_score=0):

        self.strategy = strategy
        self.score = start_score
        self.play_tally = []
        self.action = action

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

# class CopyCat(BaseCharacter):

#     def play(self):
#         self.play_tally.append(self.action)
#         if self.play_tally == []:
#             return self.action
#         else
#             return


if __name__ == '__main__':

    type_A = BaseCharacter('cheat', action=0)
    type_B = BaseCharacter('cooperate', action=1)

    action_tally = []

    for i in range(4):
        action_tally.append(type_A.round(type_B)[1])
        # print('detective:', type_A.action)
        # print('grudger:', type_B.action)
    print(action_tally)
    # print(type_A.score)
    # print(type_B.score)
