
# Ask roll the dice?
# if user  select y print the dies number
# if user select n print the thank you message and terminate the program
# if user select other then y and n  print the Invalid choice

import random


while True:
    choice = input("Roll the dice ? (y/n):").lower()

    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1},{die2})")
    elif choice == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!")
