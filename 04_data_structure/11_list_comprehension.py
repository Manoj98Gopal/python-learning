items = [
    ("product1", 10),
    ("product2", 30),
    ("product3", 7),
    ("product4", 44),
    ("product5", 4),
]

# using map functions
map_result = list(map(lambda item:item[1],items))
# using comprehension
comprehension_map = [item[1] for item in items]


# using filter function
filter_result = list(filter(lambda item:item[1] >= 10,items))
# using comprehension
comprehension_filter = [item for item in items if item[1] >= 10]



print("map result :", map_result)
print("comprehension map result :", comprehension_map)

print("filter result :", filter_result)
print("comprehension filter result :", comprehension_filter)