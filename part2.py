class Customer:
    def __init__(self):
        self.menu = {}
        self.order = {}

    def viewMenu(self):
        print("Menu:")
        if self.menu:
            for item, price in self.menu.items():
                print(f"{item}: ${price}")
        else:
            print("The menu is empty.")

    def addFood(self, item):
        if item in self.menu:
            if item in self.order:
                self.order[item] += 1
            else:
                self.order[item] = 1
            print(f"{item} added to your order.")
        else:
            print(f"{item} is not available in the menu.")

    def deleteFood(self, item):
        if item in self.order:
            self.order[item] -= 1
            if self.order[item] == 0:
                del self.order[item]
            print(f"{item} removed from your order.")
        else:
            print(f"{item} is not in your order.")

# Example usage:
customer = Customer()

# User input for menu items and prices
menu_size = int(input("Enter the number of items in the menu: "))
for _ in range(menu_size):
    item, price = input("Enter item and price (separated by space): ").split()
    customer.menu[item] = float(price)

customer.viewMenu()

# User input for adding items to the order
add_order = input("Would you like to add an item to your order? (yes/no): ").lower()
while add_order == "yes":
    item = input("Enter the item you want to add: ")
    customer.addFood(item)
    add_order = input("Would you like to add another item to your order? (yes/no): ").lower()

print("Current order:", customer.order)

# User input for deleting items from the order
delete_order = input("Would you like to delete an item from your order? (yes/no): ").lower()
while delete_order == "yes":
    item = input("Enter the item you want to delete: ")
    customer.deleteFood(item)
    delete_order = input("Would you like to delete another item from your order? (yes/no): ").lower()

print("Current order:", customer.order)