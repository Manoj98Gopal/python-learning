# global scope
message = "Good Morning"
message1 = "Good Morning"


def update_greeting(name):
    # local scope
    # it is not possible to update global variable
    message = name
    
    

update_greeting("Good Evening")
print("message :",message)


# if we need to update global variable intentionally  we need to use  global keyword inside the function
def update_global(name):
    global message1;
    message1 = name
    
    
    

update_global("Good Evening")
print("global variable :",message1)


# note: What ever we create variable inside the function python will create memory space  and  after completing the function garbage collector will free the space