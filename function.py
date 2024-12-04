def calculate_discount(price,discount_percent):
    discount_percent=discount_percent/100
   
    if discount_percent>=0.2:
        return price-(price*discount_percent)
    else:
        return price
price=float(input("The price of the item is:"))
discount_percent=float(input("The discount offered on the item:"))
finalprice=calculate_discount(price,discount_percent)
print(f"The final price is: {finalprice}")
    