
letters = ["a","b","c"]

print("Normal looping")
# we can iterate like this 
for letter in letters:
    print(letter)
    

print("using enumerate with index")
# if we want index also use enumerate
for letter in enumerate(letters):
    # here I am getting tuples
    print(letter) 
    
    
    
print("using enumerate with index")
# if we want index also use enumerate
for letter in enumerate(letters):
    # we can access like this also
    print(letter[0],letter[1])
    


print("using unpacking we can access tuples")
for index,letter in enumerate(letters):
    # we can access like this also
    print(index,letter)
    
    
exam = (1,2,3,4,5)
print(exam[1])

# unpack tuples
first,second,*other = exam
print(first)
print(second)
print(other) # here it will convert to list