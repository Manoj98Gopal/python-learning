items = [
    ("product1", 10),
    ("product2", 30),
    ("product3", 7),
    ("product4", 44),
    ("product5", 4),
]

# filter this above list based on price above 10 

basic_filtered_price_list = []

# basic way
for item in items:
    if item[1] >= 10:
        basic_filtered_price_list.append(item)

print("basic filter result :",basic_filtered_price_list)


# normal function way
def check_price(item):
    return item[1] >= 10


normal_func_with_filter_func = list(filter(check_price,items))

print("filter function using normal:",normal_func_with_filter_func)

# using lambda function
lambda_func_with_filer_func = list(filter(lambda item:item[1] >= 10,items))
print("Lambda function result :",lambda_func_with_filer_func)