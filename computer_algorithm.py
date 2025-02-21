class ComputerAlgorithm:
    def __init__(self) -> None:
        self.winner_moves = {"r": "s", "s": "p", "p": "r"}

    def winner(self, hand1: str, hand2: str) -> int:
        """
        returns:
        1 -> computer wins;
        0 -> tie;
        -1 -> player wins;
        """

        if hand1 == hand2:
            return 0
        return 1 if self.winner_moves[hand1] == hand2 else -1

    def best_hand(self, computer_hands: list[str], player_hands: list[str]) -> str:
        best_choice = None
        best_outcome = -1  # the worst that could happen is computer loses

        for computer_hand in computer_hands:
            worst_case = min(
                self.winner(computer_hand, player_hand) for player_hand in player_hands
            )

            if worst_case == 1:
                return computer_hand
            elif worst_case == 0 and best_outcome < 0:
                best_choice = computer_hand
                best_outcome = 0
            elif worst_case == -1 and best_choice == None:
                best_choice = computer_hand
        return best_choice
