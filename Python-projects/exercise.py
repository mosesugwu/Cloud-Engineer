# Variables
num_coffees = float(100) # floating-point variable
avg_price = float(2.5) # floating-point variable
coffee_shop_name = "Caffeine Buzz" # string variable
is_open = True # Boolean variable

# List
menu = ["Espresso", "Cappo", "Latte"]

# Dictionary
sales = {
    "Espresso": 50,
    "Cappo": 30,
    "Latte": 20 
}

# Tuple
specials = ("Mocha", "Iced Coffee", "Macchiato")

# Set
loyal_customers = {"Moses", "Mike", "Kimbo"}

# Print values
print("Coffee shop name:", coffee_shop_name)
print("Number of coffees sold today:", num_coffees)
print("Average price per coffee:", avg_price)
print("Is the coffee shop open?", is_open)
print("Menu:", menu)
print("Sales:", sales)
print("Specials:", specials)
print("Loyal Customers:", loyal_customers)

# Operations
total_revenue = num_coffees * avg_price # multiplication operation
print("Total revenue generated:", total_revenue)

# Boolean
if is_open:
    print("The coffee shop is currently open.")
else:
    print("The coffee shop is currently closed.")

print("Second coffee in the menu:", menu[1]) # Accessing list item by index
print("Number of sales for 'Cappo':", sales["Cappo"]) # Accessing dictionary value by key
print("Number of specials available:", len(specials)) # Length of tuple
if "Moses" in loyal_customers: # checking set membership
    print("Moses is a loyal customer.")
else:
    print("Moses is not a loyal customer.") 
