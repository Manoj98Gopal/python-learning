
def calculate_xfactor(age):
    if age <= 0 :
        raise ValueError("Age shouldn't be a zero or negative")
    print("working fine....")
    return 10 / age


try:
    calculate_xfactor(0)
except Exception as e:
    print("error:",e)