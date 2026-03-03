numbers = [1,2,3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

print("Normal assign :",first,second,third)

# same thing we can achieve using list unpacking
num1, num2, num3 = numbers
print("list unpacking :",num1,num2,num3)


# if we have so many number, we need to access only first and second index value, how to achieve this 
example = [2,3,4,3,5,6,7,54,33]
num1, num2, *other = example
print(num1,num2)
print(other)


# access first and last index in the middle leave it 
firstValue,*middle,lastValue = example
print(firstValue,lastValue)
print(middle)