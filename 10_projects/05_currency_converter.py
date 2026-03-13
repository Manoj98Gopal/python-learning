
USD = "usd"
EUR = "eur"
CAD = "cad"
INR = "inr"


def get_user_amount():
    while True:
        try:
            user_amount = int(input("Enter the amount: "))
            if user_amount <= 0:
                raise ("Amount should be more then 1")
            return user_amount
        except Exception as e:
            print("Invalid amount")


def get_currency(type):
    CURRENCY_LIST = (USD, INR, CAD, EUR)

    while True:
        selected_currency = input(
            f"{type} currency (USD / INR / CAD / EUR) :").lower()
        if selected_currency in CURRENCY_LIST:
            return selected_currency
        else:
            print("Invalid currency")


def get_target_value(source, target, user_amount):
    CURRENCY_DATA = {
        USD: {
            EUR: 0.869,
            CAD: 1.36,
            INR: 92.39,
        },
        EUR: {
            USD: 1.15,
            CAD: 1.57,
            INR: 106.3,
        },
        CAD: {
            EUR: 0.637,
            USD: 0.735,
            INR: 67.7,
        },
        INR: {
            EUR: 0.00940566,
            CAD: 0.014766,
            USD: 0.010822,
        },
    }

    if source == target:
        print(f"You selected source and target currency same {source}")
        return 1 * user_amount

    one_of_target_value = CURRENCY_DATA[source][target]
    result = one_of_target_value * user_amount
    return result


def start_currency_converter():
    amount = get_user_amount()
    source = get_currency("Source")
    target = get_currency("Target")
    determine_target_value = get_target_value(source, target, amount)
    print(f"{amount} {source.upper()} is equal to {determine_target_value}")



if __name__ == "__main__":
    start_currency_converter()
