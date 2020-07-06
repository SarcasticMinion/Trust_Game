import random

TRUST_DICT = {
    'cheat': 0,
    'cooperate': 1
}


def trust_result(first_inp, second_inp):

    results_dict = {
        (1, 1): (2, 2),
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

    print(trust_round())
