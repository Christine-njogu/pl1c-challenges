import sys
import random


def main():
    print("\nRock, Paper, Scissors game")
    print("-" * 70)
    print("This is a game of two players where both players choose either of 'rock', 'paper' or 'scissors'. "
          "Each time there's a winner based on the following rules: \n-rock vs paper: paper wins because a rock can be "
          "wrapped in a paper\n-rock vs scissors: rock wins because a rock can crush a pair of scissors\n-paper vs "
          "scissors: scissors wins because it can cut the paper")
    while True:
        game = ['rock', 'paper', 'scissors']
        comp_play = random.choices(game, k=1)
        user_play = input("\nChoose your pick of rock, paper or scissors: ")
        print(f"Computer's pick: {comp_play}")
        if (user_play == "rock" and comp_play[0] == "scissors") or (user_play == "paper" and comp_play[0] == "rock") or (
                user_play == "scissors" and comp_play[0] == "paper"):
            print("You win")
        elif (user_play == "rock" and comp_play[0] == "paper") or (user_play == "scissors" and comp_play[0] == "rock") or (
                user_play == "paper" and comp_play[0] == "scissors"):
            print("You lose")
        elif user_play == comp_play[0]:
            print("You draw")
        else:
            print("Invalid entry")
        end_game = input("\nTo end game press x: ")
        if end_game == "x":
            break


if __name__ == "__main__":
    sys.exit(main())