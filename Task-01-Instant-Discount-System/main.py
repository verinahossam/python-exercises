# Instant Discount System

# Welcome Message
message = "Welcome to Our System"
print(message.center(30))

# Get the purchase value from the user
purchase_value = int(input("Enter the purchase value: ").strip())

# Check the discount percentage
if purchase_value < 100:
    discount_value = 0
elif 100 <= purchase_value < 500:
    discount_value = 10
else:
    discount_value = 20

# Calculate the final value after applying the discount
final_value = purchase_value * (100 - discount_value) / 100

# Display the results
print(" Receipt ".center(30, "="))
print(f"Purchase Value: {purchase_value}")
print(f"Discount: {discount_value}%")
print(f"Final Price: {final_value}")
