from twoparts import twoParts

class Game:
    def __init__(self,state,player=True):
        self.state = state
        self.player = player

MAX = 1

def possible_actions(node):
    actions = []
    state = node.state
    for pile in state :
        if (pile>2):
            two_parts = twoParts(pile)  # 7 => [[1, 6], [2, 5], [3, 4]]
            for couple in two_parts:
                new_state = [x for x in state if x != pile] # remove element from list
                new_state.append(couple[0])
                new_state.append(couple[1])
                actions.append(new_state)
    return actions


def utility(node):
    if node.player == MAX: #MAX is stuck -> loss
        return -1
    return 1


def print_seq(seq):
    seq.toString()


