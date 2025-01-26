import random

def winner(player_1, player_2):
    if player_1 == player_2:
        return "Tie"
    elif (player_1 == "r" and player_2 == "s") \
        or (player_1 == "p" and player_2 == "r") \
        or (player_1 == "s" and player_2 == "p"):
            return "Player wins"
    else:
        return "computer wins"

def game():
    while True:
        choices= ['r', 'p', 's']
        player_hand1:str = input("Enter Your First Hand (R)ock, (P)aper, (S)cissors -> ").lower()

        if player_hand1 not in choices:
            print("invalid choice")
            continue
        
        player_hand2:str = input("Enter Your Second Hand (R)ock, (P)aper, (S)cissors -> ").lower()

        if player_hand1 not in choices:
            print("invalid choice")
            continue

        computer_hand1:str = random.choice(choices)
        computer_hand2:str = random.choice(choices)

        print(f"The computer's choice -> {computer_hand1}, {computer_hand2}")
        
        while True:
            remove_hand:int = int(input("Enter which hand do you want to minus 1 or 2 ) -> " ))
            if remove_hand in [1,2]:
                break
            else:
                print("enter 1 or 2 to remove the respective hand -> ")

        player_hand = player_hand1 if remove_hand == 2 else player_hand2

        remove_hand_computer = random.choice([1,2])

        computer_hand = computer_hand1 if remove_hand_computer == 2 else computer_hand2
        
        print(winner(player_hand, computer_hand))

        play_again = input("Do you want to play again? (y/n) -> ").lower()
        if play_again != 'y':
            break


game()

