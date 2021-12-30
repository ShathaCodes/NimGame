from math import inf
from game import Game, possible_actions, utility

MAX = 1
nbr_developed_nodes =0
nbr_elagage =0
sequences = []
sequence = []

def minimaxab(node,alpha,beta):
    actions = possible_actions(node)
    global nbr_elagage
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
            score = minimaxab(new_node,alpha,beta)
            best = max(best,score)
            alpha = max(best,alpha)
            if alpha >= beta :
                nbr_elagage = nbr_elagage + 1
                break
        return best

    else:
        best = +inf
        for action in actions:
            new_node = Game(action,-node.player)
            score = minimaxab(new_node,alpha,beta)
            best = min(best,score)
            beta = min(best,beta)
            if alpha >= beta :
                nbr_elagage = nbr_elagage + 1
                break
        return best

def play_ab(number,first_player):

    initial_node = Game(state=[number],player=first_player)

    result = minimaxab(initial_node,-inf,inf)

    print()
    
    if result == 1:
        print("The winner is MAX")
    else:
        print("The winner is MIN")

    print("Sequences of actions: ")
    for seq in sequences:
        print('\t'.join(str(e.state) for e in seq))
    print("Number of developed nodes: " , nbr_developed_nodes)
    print("Number of elagage: " , nbr_elagage)