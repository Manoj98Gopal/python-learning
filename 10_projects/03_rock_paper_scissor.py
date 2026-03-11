# Ask user to choose these three options like (Rock, paper, scissor)
# If user enter wrong thing show invalid option and again give option to select
# If user select any option, show  system selected, and user selected, and result
# After showing result ask user to do want to continue and not, give options like yes or no
# If user select yes terminate from the game other wise show again options

import random

options = ['r', 'p', 's']

fav_icon = {
    "r": "🪨",
    "p": "📝",
    "s": "✂️"
}

results = {
    "r,s": 0,
    "r,p": 1,
    "s,r": 1,
    "s,p": 0,
    "p,s": 1,
    "p,r": 0,
    "p,p": 2,
    "s,s": 2,
    "r,r": 2
}


def system_select():
    result = random.choice(options)
    return result


def check_result(user_chose, system_chose):

    index = results[f"{user_chose},{system_chose}"]

    if index:
        return "You lose!"
    if index == 2:
        return "Both are equal!"
    else:
        return "You win!"


while True:

    user_chose = input("Rock, paper, or scissors? (r/p/s):").lower()

    if user_chose not in options:
        print("Invalid option!")
    else:
        system_chose = system_select()
        user_result = check_result(user_chose, system_chose)
        print("System selected :", fav_icon[system_chose])
        print("Your selected :", fav_icon[user_chose])
        print(user_result)

        want_to_play = input("Continue ? (y/n) :").lower()

        if want_to_play == "n":
            break
