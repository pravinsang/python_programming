def calculate_discounted_price(original_price, discount):
    assert discount >= 0 and discount <= 100, "Invalid discount percentage!"
    discounted_price = original_price - (original_price * (discount / 100))
    return discounted_price

price = 1000
discount_percentage = 120

final_price = calculate_discounted_price(price, discount_percentage)
print(f"The final price after a {discount_percentage}% discount is: Rs. {final_price}")
