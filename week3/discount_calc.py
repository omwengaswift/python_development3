# 1.
def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount.
    Only applies discount if discount_percent >= 20.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price   # no discount applied


# 2.
# Ask user for inputs
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
