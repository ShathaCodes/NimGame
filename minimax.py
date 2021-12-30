from math import inf
from game import Game, possible_actions, utility

MAX = 1
nbr_developed_nodes =0

sequences = []
sequence = []

def minimax(node):
    actions = possible_actions(node)
    global nbr_developed_nodes
    global sequence
    global sequences
    sequence.append(node)
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    if actions == []:
        score = utility(node)
        sequences.append(sequence)
        sequence = []
        return score

    if node.player == MAX:
        best = -inf
        for action in actions:
            new_node = Game(action,-node.player)
            score = minimax(new_node)
            best = max(best,score)
        return best

    else:
        best = +inf
        for action in actions:
            new_node = Game(action,-node.player)
            score = minimax(new_node)
            best = min(best,score)
        return best


def play(number,first_player):
    global nbr_developed_nodes
    global sequence
    global sequences

    initial_node = Game(state=[number],player=first_player)

    result = minimax(initial_node)
    
    print()
    
    if result == 1:
        print("The winner is MAX")
    else:
        print("The winner is MIN")

    print("Sequences of actions: ")
    for seq in sequences:
        print('\t'.join(str(e.state) for e in seq))
    print("Number of developed nodes: " , nbr_developed_nodes)
    
