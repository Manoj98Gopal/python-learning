
# here we handling different exception


try:
    age = int(input("age :"))
    factor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print("You entered wrong age")
    print("error :", error)
# we can use like multiple exception if want to test uncomment the below one
# except ZeroDivisionError as error:
#     print("age shouldn't be Zero")
else:
    print("You entered age is :", age)
    print("factor result :", factor)
