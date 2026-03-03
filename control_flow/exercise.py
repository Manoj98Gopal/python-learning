
length = 0

for number in range(1, 10):
    if number % 2 == 0:
        length += 1
        print(number)
        
        
print(f"We have {length} even numbers")
