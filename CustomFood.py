# Custom Food
# Chris Dixon
# 02/16/2024

"""The following program is designed to allow the user to customize their pizza by choosing one of the available
pizzas as a base, then choosing the topping for that order, and then the total order price is calculated and displayed
below. The user can also add another order to that as well."""

# Available Pizzas
available_pizzas = ['Meat Lover Pizza', 'Cheesy Cheese Pizza', 'Vegetarian Pizza', 'Shinobi Swirls Plate',
                    'Chili Dog Pizza', 'Spaghetti Pizza']

# Available Toppings
available_toppings = ['Anchovies', 'Mushrooms', 'Onions', 'Green peppers', 'Bacon', 'Ham', 'Extra cheese']

# Pizza Prices
pizza_prices = {'Meat Lover Pizza': 6.99, 'Cheesy Cheese Pizza': 5.25, 'Vegetarian Pizza': 4.20,
                'Shinobi Swirls Plate': 8.99, 'Chili Dog Pizza': 8, 'Spaghetti Pizza': 9.99}

# Topping Prices
topping_prices = {'Anchovies': 0.99, 'Mushrooms': 0.99, 'Onions': 1, 'Green peppers': 2, 'Bacon': 3, 'Ham': 4,
                  'Extra cheese': 3}


sub_total = []  # Sub Total

final_order = {}    # Final Order

total_price = sum(sub_total)    # Total Price


print("Custom Pizza menu")

# Order pizza
order_pizza = True
while order_pizza:
    while True:
        print("\n Available pizzas: ")
        print(available_pizzas)
        print("-------------------------------------------------------")
        pizza = input("Which pizza would you like to order? ")
        if pizza in available_pizzas:
            sub_total.append(pizza_prices[pizza])
            print(f"\n{pizza} ordered.")
            break
        if pizza not in available_pizzas:
            print(f"\nInvalid")

    # Order toppings
    order_topping = True
    while order_topping:
        print("\n Available toppings: ")
        print(available_toppings)
        print("-------------------------------------------------------")
        topping = input("Which one would you like to add? ")
        if topping in available_toppings:
            final_order.setdefault(pizza, [])
            final_order[pizza].append(topping)
            sub_total.append(topping_prices[topping])
            print(f"\n{topping} added.")
            break
        else:
            print(f"\nInvalid")

    # Check Order
    check_order = True
    while check_order:
        order_correct = input("\nIs this correct? yes/no \n")
        if order_correct == "yes":
            check_order = False
            order_pizza = False
        if order_correct == "no":
            print(final_order)
            choice_AddRemove = input("Would you like to add more? yes/no \n")
            if choice_AddRemove == "yes":
                check_order = False
            else:
                print("\nInvalid")

# Display Final Order
print("\n-------------------------------------------------------")
print(f"Final order: {final_order}")
print(f"Total order price: ${total_price: .2f}")
print("-------------------------------------------------------")
