import random

from computer_algorithm import ComputerAlgorithm


class RockPaperScissorsMinusOne:
    """
    A class that implements Rock Paper Scissors Minus One game.
    
    This is a variant of Rock Paper Scissors where both players start with two hands
    and must remove one before the final comparison. The computer uses an AI algorithm
    to choose its best move.
    """

    def __init__(self) -> None:
        """
        Initialize the game with an AI opponent and valid game choices.
        """
        self.ai = ComputerAlgorithm()
        self.choices = ["r", "s", "p"]
        self.choice_name = {"r": "rock", "s": "scissors", "p": "paper"}

    def get_player_hands(self) -> list[str]:
        """
        Get two hand choices from the player via console input.
        
        Returns:
            list[str]: List containing the player's two hand choices.
        """
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
        """
        Generate two random hands for the computer.
        
        Returns:
            list[str]: List containing two random choices for the computer.
        """
        return [random.choice(self.choices) for _ in range(2)]

    def determine_winner(self, computer_hand: str, player_hand: str) -> str:
        """
        Determine the winner of a single round.
        
        Args:
            computer_hand (str): The computer's chosen hand
            player_hand (str): The player's chosen hand
            
        Returns:
            str: A string indicating the winner of the round
        """
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
        """
        Play a single round of Rock Paper Scissors Minus One.
        
        Gets hands from both players, lets the player choose which hand to remove,
        and determines the winner of the round.
        """
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
        """
        Start the game loop.
        
        Continuously plays rounds until the player chooses not to continue.
        """
        while True:
            self.play_round()
            play_again: str = input("Do you want to play again ? [(Y)es, (N)o]").lower()
            if play_again != "y":
                print("Thnaks for playing")
                break
            print('\n')


if __name__ == "__main__":
    S = RockPaperScissorsMinusOne().start()
