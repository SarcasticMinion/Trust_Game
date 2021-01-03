import random
import numpy as np
from sklearn.metrics import log_loss

TRUST_DICT = {
    'cheat': 0,
    'cooperate': 1
}


def trust_result(first_inp, second_inp, payoff):

    results_dict = {
        (1, 1): (payoff, payoff),
        (1, 0): (-1, 3),
        (0, 1): (3, -1),
        (0, 0): (0, 0)
    }

    return results_dict[(first_inp, second_inp)]


def trust_round():
    player_action = TRUST_DICT[input('Please choose to either COOPERATE'
                                     ' (put in a coin) or CHEAT '
                                     '(not put in a coin):\n').lower()]

    computer_action = random.choice([0, 1])

    return trust_result(player_action, computer_action)



if __name__ == '__main__':

    # print(trust_round())
    # y_hat = [
    #     [1, 2, 1],
    #     [1, 3, 1],
    #     [1, 4, 1],
    #     [1, 5, 1]
    # ]
    # yvals = [
    #     [y for y in batch]
    #     for batch in y_hat
    # ]

    # print(yvals)
    # prob = [0.2, 0.5, 0.1, 0.15, 0.05]
    # temp = max(range(len(prob)), key=lambda i: prob[i])
    # print(temp)
    # y = [0, 1, 2, 3, 4, 1, 2, 0, 1, 4]
    # for i in y:
    #     one_hot = [int(j == i) for j in range(5)]
    #     print(one_hot)
    y_temp = [
        [[0.245, 0.090, 0.665],
        [0.665, 0.245, 0.090],
        [0.090, 0.665, 0.245]],
        [[0.245, 0.090, 0.665],
        [0.665, 0.245, 0.090],
        [0.090, 0.665, 0.245]]
    ]

    # y_true = [0, 1, 2]

    y = np.array(y_temp)
    # print(y.shape)
    print(np.linalg.norm(y, axis=0))

    # print(log_loss(y_true, y_temp))