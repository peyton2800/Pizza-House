# Cancel Order
# Chris Dixon
# 02/16/2024

"""The following program is designed to allow the user to remove orders from the list"""

# Food Menu
food_menu = {"Pizza", "Wings", "Fries", "Chips", "Soda", "Juice", "Water"}

# Current Order
current_order = [["Pizza", "Fries", "Soda"], ["Wings, Chips, Juice"]]

# Order Number
order_number = {'Pizza", "Fries", "Soda': 1, 'Wings, Chips, Juice': 2}


# Delete Order
def del_order():
    while True:
        print("What order do you want to remove?", "1 or 2? ")
        order = int(input())
        if order == 1 or order == 2:
            choice = (order - 1)
            del current_order[choice]
            print("Order", order, "deleted.")
        elif order != 1 or order != 2:
            print("Order does not exist")
        else:
            print("Sorry, but we don't serve that. Please try again.")
        return current_order


# Output Order
def output_order(order_list):
    ordersList = []
    print(f"\nYour final order is...")
    for order in order_list:
        ordersList.append(order)
    print(ordersList)


# Main
def main():
    print(f"Current Orders: ", current_order, "\n")
    order = del_order()
    output_order(order)
    print(f"\nCurrent Orders: ", current_order, "\n")
    choice = input(f"Would you like to remove another order? Yes/No \n")
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
