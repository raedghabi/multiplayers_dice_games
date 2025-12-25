# import random module
import random

# welcome message and game instructions
print("-------------------------------------")
print("Welcome to my Dice Game!")
print("1 : The objective of the game is to be the first player to reach 10 points.")
print("2 : On your turn, you can roll the dice as many times as you like.")
print("3 : Each roll adds to your turn total, but if you roll a 1, your turn ends and you score no points for that turn.")
print("4 : You can choose to 'hold' at any time to add your turn total to your overall score.")
print("     Good luck! Let's start the game!")
print("-------------------------------------")

input("press enter to start the game")

# function to roll the dice
def roll():
    return random.randint(1, 6)

def about():
    print("-------------------------------------")
    print("            Game Over!")
    print("Thank you for playing my Dice Game!")
    print("    Developed by: read ghabi")
    print("-------------------------------------")

# get number of players
while True:
    player = input("enter the number of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
    print("Invalid input. Please enter a number between 2 and 4.")

# initialize players' scores
players_score = [0 for _ in range(player)]
max_score = 10
game_over = False

# main game loop
while not game_over:
    for i in range(player):
        current_score = 0

        roll_input = input(f"player {i+1}, do you want to roll the dice? (y/n): ")
        if roll_input.lower() != 'y':
            print(f"player {i+1} skipped their turn.")
            print(f"player {i+1}'s total score is {players_score[i]}")
            continue

        while True:
            dice_value = roll()
            print("you rolled a", dice_value)

            if dice_value == 1:
                print("you rolled a 1, your turn is over and you score no points this turn.")
                current_score = 0
                break
            else:
                current_score += dice_value
                print("your score for this turn is", current_score)

                # Immediate winner check
                if players_score[i] + current_score >= max_score:
                    players_score[i] += current_score
                    print(f"player {i+1} wins with a score of {players_score[i]}")
                    about()
                    game_over = True
                    break

                decision = input("do you want to roll again or hold? (r/h): ")
                if decision.lower() == 'h':
                    break
                elif decision.lower() != 'r':
                    print("Invalid input. Holding by default.")
                    break

        if game_over:
            break

        players_score[i] += current_score
        print(f"player {i+1}'s total score is {players_score[i]}")

    if game_over:
        break
