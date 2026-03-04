items = [
    ("product1", 10),
    ("product2", 30),
    ("product3", 1),
    ("product4", 44),
]

# create a new list and add only prices not product
# basic way to achieve this 
basic_prices = []

for product,price in items:
    basic_prices.append(price)
    
print("basic way transformation :", basic_prices)

# using map function how to achieve same functionality
map_result = map(lambda item:item[1],items)  #here we are getting object <map object at 0x76e6de5e3f10>

# convert object into list using list function
map_prices = list(map_result)

print("map result :",map_result)
print("map converted result :",map_prices)