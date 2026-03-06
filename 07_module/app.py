from ecommerce.shopping import sales




print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__loader__)


sales.call_to_customer()
sales.cal_ship()
sales.get_data()
