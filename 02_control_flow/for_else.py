
successful = False

for number in range(3):
    print(f"Attempt {number + 1}")
    if successful:
        print("Sended successfully!")
        break;
else:
    print("Attempt 3 times not sended successfully")