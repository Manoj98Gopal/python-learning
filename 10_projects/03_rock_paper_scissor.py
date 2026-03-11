# Ask user to choose these three options like (Rock, paper, scissor)
# If user enter wrong thing show invalid option and again give option to select
# If user select any option, show  system selected, and user selected, and result
# After showing result ask user to do want to continue and not, give options like yes or no
# If user select yes terminate from the game other wise show again options

import random

ROCK = "r"
PAPER = "p"
SCISSOR = "s"

options = {ROCK: "🪨", PAPER: "📝", SCISSOR: "✂️"}
choices = tuple(options.keys())


def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s):").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")


def display_choice(user_choice, computer_choice):
    print(f"You chose {options[user_choice]}")
    print(f"Computer chose {options[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You Win!")
    else:
        print("You Lose")


def play_game():

    while True:

        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choice(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue ? (y/n) :").lower()
        if should_continue == "n":
            break


play_game()





# This is my code

# option = ['r', 'p', 's']

# fav_icon = {"r": "🪨", "p": "📝", "s": "✂️"}

# results = {
#     "r,s": 0,
#     "r,p": 1,
#     "s,r": 1,
#     "s,p": 0,
#     "p,s": 1,
#     "p,r": 0,
#     "p,p": 2,
#     "s,s": 2,
#     "r,r": 2
# }


# def system_select():
#     result = random.choice(option)
#     return result


# def check_result(user_chose, system_chose):

#     index = results[f"{user_chose},{system_chose}"]

#     if index:
#         return "You lose!"
#     if index == 2:
#         return "Both are equal!"
#     else:
#         return "You win!"


# def get_computer_choice():

#     computer_choice = ""


# def play_game():

#     while True:

#         user_choice = input("Rock, paper, or scissors? (r/p/s):").lower()

#         if user_choice not in option:
#             print("Invalid option!")
#         else:
#             system_chose = system_select()
#             user_result = check_result(user_choice, system_chose)

#             print("System selected :", fav_icon[system_chose])
#             print("Your selected :", fav_icon[user_choice])

#             print(user_result)

#             want_to_play = input("Continue ? (y/n) :").lower()
#             if want_to_play == "n":
#                 break


# play_game()
