# cleaning up

try:
    age = int(input("age :"))
    factor = 10 / age
except (ValueError,ZeroDivisionError) as err:
    print(err)
else:
    print("function doesn't have any error")
finally:
    # we can clean anything here  if exception occurs  either not  finally block will execute.
    print("finally block executed.")
