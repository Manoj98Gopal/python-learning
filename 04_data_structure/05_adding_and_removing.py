letters = ["a","b","c"]


# Adding 
letters.append("d") #it will add the item at the last
letters.insert(0,"-") #it will add the item at the specific index


# Removing 
letters.pop() #it will remove last item
letters.pop(0) #it will remove specific index of items
letters.remove("b") #it will remove specific value first occurrence of the list 
del letters[1] #it is also one type of method to remove items from the list
del letters[0:3] #In this method we can remove multiple items from the list
letters.clear() #It is used to empty the list


print(letters) 