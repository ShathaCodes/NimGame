from minimax import play
from minimaxab import play_ab


def main():
    while(True):
        print("Which algorithm would you like to choose :")

        print("\n\t1/ MINIMAX")
        print("\t2/ Alpha Beta")    

        algorithm = int(input("\n_ : "))

        if algorithm ==1 :
            play()
        else:
            play_ab()
        
        print("\nWanna give it another try ? ")
        retry = input("\n_ : ")
        if "N" in retry.upper():
            break

if __name__ == '__main__':
    main()