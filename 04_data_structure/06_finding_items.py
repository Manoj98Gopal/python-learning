letters = ["a","b","c","d"]

print(letters.index("b"))

# print(letters.index("e"))   if it is not in the list it will throw the error, we can overcome this problem using  "in or count operator"

# using "in or count" method we can overcome the error problem

print("count method :",letters.count("e"))
print("in method :","e" in letters)

if "e" in letters:
    print(letters.index("e"))
    
if letters.count("e"):
    print(letters.index("e"))