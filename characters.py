from trust_basics import trust_result

class Character():

    def __init__(self, strategy, start_score, action):

        self.strategy = strategy
        self.score = start_score
        self.play_tally = []
        self.action = action

    def play(self, other):
        return self.action

    def round(self, other):
        results = trust_result(self.action, other.action)
        self.score += results[0]
        other.score += results[1]

if __name__ == '__main__':

    type_A
