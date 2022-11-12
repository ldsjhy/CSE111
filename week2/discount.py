from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
print(day_of_week)

subtotal = float(input("Please enter the subtotal: "))


if int(day_of_week) == 2 and subtotal >= 50 or int(day_of_week) == 1 and subtotal >= 50:

    discount_amount = subtotal * 0.1
    discounted_price = subtotal * 0.9
    total_discounted_price = discounted_price * 1.06
    sales_tax = discounted_price * 0.06
    
    print(f"Discount amount: {discount_amount:.2f}")
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total_discounted_price:.2f}")

else:
    
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax
    
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")