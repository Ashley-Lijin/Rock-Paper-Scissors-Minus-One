class ComputerAlgorithm:
    """
    Yo fam! 🎮 This class is all about playing Rock Paper Scissors like a boss!
    It helps figure out the best moves and who's winning the game.
    
    Think of it as your gaming bestie that knows all the RPS strats!
    """

    def __init__(self) -> None:
        """
        Sets up the winning moves dictionary - it's like a cheat sheet fr fr!
        'r' beats 's', 's' beats 'p', and 'p' beats 'r'
        """
        self.winner_moves = {"r": "s", "s": "p", "p": "r"}

    def winner(self, hand1: str, hand2: str) -> int:
        """
        Spills the tea on who won the round! 🏆
        
        Args:
            hand1 (str): First player's move (computer usually)
            hand2 (str): Second player's move
        
        Returns:
            int: The outcome be like:
            1 -> computer wins (W)
            0 -> it's a tie (mid)
            -1 -> player wins (L)
        """
        if hand1 == hand2:
            return 0
        return 1 if self.winner_moves[hand1] == hand2 else -1

    def best_hand(self, computer_hands: list[str], player_hands: list[str]) -> str:
        """
        No cap, this method finds the most OP move for the computer! 💯
        
        It's like playing chess - thinks ahead about what the player might do
        and picks the move that's least likely to get rekt.
        
        Args:
            computer_hands (list[str]): All possible moves the computer can make
            player_hands (list[str]): All possible moves the player might make
        
        Returns:
            str: The most fire move for the computer rn
        """
        best_choice = None
        best_outcome = -1  # the worst that could happen is computer loses (big L)

        for computer_hand in computer_hands:
            worst_case = min(
                self.winner(computer_hand, player_hand) for player_hand in player_hands
            )

            if worst_case == 1:
                return computer_hand  # found a guaranteed W, let's get this bread!
            elif worst_case == 0 and best_outcome < 0:
                best_choice = computer_hand  # at least we won't lose, better than nothing fr
                best_outcome = 0
            elif worst_case == -1 and best_choice == None:
                best_choice = computer_hand  # we down bad but need something to play
        return best_choice
