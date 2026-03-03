# AND  both condition should be true
# OR   ether one condition should be true
# NOT  it revers the condition


high_income = True
good_credit = True
is_student = True


if (high_income or good_credit) and not is_student:
    print("Eligible")
else : 
    print("Not Eligible")
    

# ternary operator
message = "Eligible" if (high_income or good_credit) and not is_student else "Not eligible"

print("ternary result :",message)


# chaining comparison operator
# age should be between the 16 to 27

age = 18

if age >= 18 and age < 27:
    print("This age is allowed")
else : 
    print("This age is not allowed")
    
if  18 <= age < 27:
    print("chining result Eligible")
else:
    print("chining result not eligible")