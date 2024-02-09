# Order Class Menu
# Chris Dixon
# 02/07/2024

"""The following program is designed to the order class for the upcoming Pizza House Pizzeria Delivery service.
It will ask the user for items, then it will add them to a list, as well as add multiple orders."""

# Food Menu

food_menu = {"Pizza", "Wings", "Fries", "Chips", "Soda", "Juice", "Water"}

# New Order Input

current_order = []


def new_order():
    while True:
        print("What would you like?")
        order = input()
        if order in food_menu:
            current_order.append(order)
        else:
            print("Sorry, but we don't serve that. Please try again.")
        if is_order_complete():
            return current_order


# Is Order Complete Process
def is_order_complete():
    print(f"Will that be all for your order? Yes/No")
    choice = input()
    if choice == "Yes":
        return True
    elif choice == "No":
        return False
    else:
        raise Exception("Invalid input")


# Output Order
def output_order(order_list):
    ordersList = []
    print("Your final order is...")
    for order in order_list:
        ordersList.append(order)
    print(ordersList)


# order_cart
order_cart = []


# Main
def main():
    order = new_order()
    output_order(order)
    order_cart.append(order)
    print(f"Current Orders: ", order_cart, "\n")
    choice = input(f"Would you like to make a new order? Yes/No \n")
    if choice == "Yes":
        main()
        return True
    elif choice == "No":
        print("Thank you for your patronage.")
        return False
    else:
        raise Exception("Invalid input")


if __name__ == "__main__":
    main()
