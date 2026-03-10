# Ask to user guess the number between 1 to 100
# If user select non-integer show "Please enter valid number"
# if user select correct number show "Congratulations and break"
# Other wise based and user enter value give hit to user  high or low


import random


selected_number = random.randint(1, 100)


while True:

    gassing_number = input("Guess the number between 1 and 100 : ")
    try:
        gassing_number = int(gassing_number)

        if gassing_number < selected_number:
            print("Too low!")
        elif gassing_number > selected_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break

    except Exception as e:
        print("Please enter valid number")
