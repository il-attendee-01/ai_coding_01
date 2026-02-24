cat /home/coder/projects/release_notes/release_notes_*import random
from enum import Enum
from typing import NamedTuple


class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class GameResult(NamedTuple):
    player_wins: int
    computer_wins: int
    ties: int


class RockPaperScissors:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0

    def _get_player_choice(self) -> Choice:
        """Get and validate player input."""
        while True:
            choice = input("\nEnter your choice (rock/paper/scissors): ").lower().strip()
            try:
                return Choice(choice)
            except ValueError:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

    def _get_computer_choice(self) -> Choice:
        """Get random choice for computer."""
        return random.choice(list(Choice))

    def _determine_winner(self, player: Choice, computer: Choice) -> str:
        """Determine the round winner."""
        if player == computer:
            return "tie"

        wins = {
            (Choice.ROCK, Choice.SCISSORS): "player",
            (Choice.SCISSORS, Choice.PAPER): "player",
            (Choice.PAPER, Choice.ROCK): "player",
        }

        return wins.get((player, computer), "computer")

    def _display_round(self, round_num: int, player: Choice, computer: Choice, result: str) -> None:
        """Display round results."""
        print(f"\n--- Round {round_num} ---")
        print(f"You chose: {player.value}")
        print(f"Computer chose: {computer.value}")

        if result == "player":
            print("You win this round!")
        elif result == "computer":
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    def _display_match_score(self) -> None:
        """Display current match score."""
        print(f"\nMatch Score - You: {self.player_wins}, Computer: {self.computer_wins}, Ties: {self.ties}")

    def play_round(self, round_num: int) -> None:
        """Play a single round."""
        player_choice = self._get_player_choice()
        computer_choice = self._get_computer_choice()
        result = self._determine_winner(player_choice, computer_choice)

        self._display_round(round_num, player_choice, computer_choice, result)

        if result == "player":
            self.player_wins += 1
        elif result == "computer":
            self.computer_wins += 1
        else:
            self.ties += 1

        self._display_match_score()

    def is_match_over(self) -> bool:
        """Check if best-of-3 match is over."""
        return self.player_wins == 2 or self.computer_wins == 2

    def display_final_result(self) -> None:
        """Display match winner."""
        print("\n" + "="*40)
        if self.player_wins == 2:
            print("🎉 You won the match!")
        else:
            print("💻 Computer won the match!")
        print(f"Final Score - You: {self.player_wins}, Computer: {self.computer_wins}, Ties: {self.ties}")
        print("="*40)

    def get_result(self) -> GameResult:
        """Return final game result."""
        return GameResult(self.player_wins, self.computer_wins, self.ties)


def main() -> None:
    """Main entry point for the game."""
    game = RockPaperScissors()
    round_num = 1

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("First to 2 wins takes the match!\n")

    while not game.is_match_over():
        game.play_round(round_num)
        round_num += 1

    game.display_final_result()


if __name__ == "__main__":
    main()
