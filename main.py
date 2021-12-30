from minimax import play
from minimaxab import play_ab


def main():
    initial_number = int(input("Give the initial number: "))

    print("\n\t1/ MAX")
    print("\t2/ MIN")    

    first_player = int(input("\nChoose the first player: "))

    if first_player == 2 :
        first_player = -1

    print("\n\t1/ MINIMAX")
    print("\t2/ Alpha Beta")    

    algorithm = int(input("\nChoose the algorithm: "))

    if algorithm ==1 :
        play(initial_number,first_player)
    else:
        play_ab(initial_number,first_player)

    


if __name__ == '__main__':
    main()