age = 17


# normal if condition
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

print(message)



# ternary if condition
newMessage = "Eligible" if age >= 18 else "Not Eligible"

print("ternary result :", newMessage)
