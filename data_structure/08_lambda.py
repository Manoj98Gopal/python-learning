# if we have tuples inside the list, how we can sort
products = [
    ("product1", 10),
    ("product2", 130),
    ("product3", 1),
    ("product4", 15),
]


# normal functions
def sort_item(item):
    return item[1]


# products.sort(key=sort_item)

# lambda functions
products.sort(key=lambda item:item[1])

print(products)