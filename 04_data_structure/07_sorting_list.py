
numbers = [33, 2, 4, 55, 11, 6, 44, 9]

numbers.sort()  # if you do like this it will modify original array
print("original list", numbers)


print("descending order sort")
numbers1 = [33, 2, 4, 55, 11, 6, 44, 9]

# sort above numbers in descending order
numbers1.sort(reverse=True)
print(numbers1)


# we have another method to sort the numbers
numbers2 = [33, 2, 4, 55, 11, 6, 44, 9]

sorted_ascending_order = sorted(numbers2)
print("using sorted function in ascending:", sorted_ascending_order)

sorted_descending_order = sorted(numbers2, reverse=True)
print("using sorted function in descending:", sorted_descending_order)


# if we have tuples inside the list, how we can sort

products = [
    ("product1", 10),
    ("product2", 130),
    ("product3", 1),
    ("product4", 15),
]


def sort_item(item):
    return item[1]


products.sort(key=sort_item)

print(products)
