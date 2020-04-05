def vatcalulate():
    price = int(input("Price : "))
    result = price+(price*7/100)
    return result
print(vatcalulate())