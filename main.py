import random

from computer_algorithm import ComputerAlgorithm


class RockPaperScissorsMinusOne:

    def __init__(self) -> None:
        self.ai = ComputerAlgorithm()
        self.choices = ["r", "s", "p"]
        self.choice_name = {"r": "rock", "s": "scissors", "p": "paper"}

    def get_player_hands(self) -> list[str]:
        player_hands = []
        for i in range(2):
            while True:
                hand: str = input(
                    f"Enter your hand {i+1} (R)ock, (P)aper, (S)cissors: "
                ).lower()

                if hand in self.choices:
                    player_hands.append(hand)
                    break
                print("Enter a valid Choice (R, P, S): ")
        return player_hands

    def get_computer_hands(self):
        return [random.choice(self.choices) for _ in range(2)]

    def determine_winner(self, computer_hand: str, player_hand: str) -> str:
        if computer_hand == player_hand:
            return "\ttie 🤝"
        elif (
            (computer_hand == "r" and player_hand == "s")
            or (computer_hand == "s" and player_hand == "p")
            or (computer_hand == "p" and player_hand == "r")
        ):
            return "\tcomputer wins!"
        else:
            return "\tyou won 🎉"

    def play_round(self):
        player_hands = self.get_player_hands()
        computer_hands = self.get_computer_hands()
        print(f"The Computer hands are -> {self.choice_name[computer_hands[0]]} and {self.choice_name[computer_hands[0]]}")
        computer_best_hand = self.ai.best_hand(
            computer_hands=computer_hands, player_hands=player_hands
        )
        while True:
            try:
                remove_hand: int = int(
                    input("Enter which hand do you want to remove -> ")
                )
                if remove_hand in [1, 2]:
                    break
                print("Invalid hand, Enter a valid hand [1,2]")
            except ValueError:
                print("Invalid character, please enter a number")

        player_final_hand = player_hands[1] if remove_hand == 1 else player_hands[0]

        print("You chose -> {}".format(self.choice_name[player_final_hand]))
        print("computer chose -> {}".format(self.choice_name[computer_best_hand]))

        print(
            "winner -> {}".format(
                self.determine_winner(player_hand=player_final_hand, computer_hand=computer_best_hand)
            )
        )

    def start(self):
        while True:
            self.play_round()
            play_again: str = input("Do you want to play again ? [(Y)es, (N)o]").lower()
            if play_again != "y":
                print("Thnaks for playing")
                break
            print('\n')


if __name__ == "__main__":
    S = RockPaperScissorsMinusOne().start()
