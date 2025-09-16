price = int(input("Enter the price of the item: "))
discount = int(input("Enter the discount percentage (0-100): "))
def calculate_discount(price, discount):
    if discount >=20:
        final_price = price * (1 - discount / 100)
        print (f"The price of after applying discount is: {final_price}")
    else:
        print(f"Discount not applicable the final price is: {price}")
calculate_discount(price, discount)
        