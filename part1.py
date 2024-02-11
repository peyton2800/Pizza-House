class Customer:
    def __init__(self):
        self.order = []

    def viewMenu(self, menu):
        print("Menu:")
        for item in menu:
            print(item)

    def addFood(self, menu, item):
        if item in menu:
            self.order.append(item)
            print(f"{item} added to your order.")
        else:
            print(f"{item} is not available in the menu.")

    def deleteFood(self, item):
        if item in self.order:
            self.order.remove(item)
            print(f"{item} removed from your order.")
        else:
            print(f"{item} is not in your order.")

# Example usage:
menu = ["Pizza", "Burger", "Fries", "Salad"]
customer = Customer()

customer.viewMenu(menu)

customer.addFood(menu, "Pizza")
customer.addFood(menu, "Sushi")

print("Current order:", customer.order)

customer.deleteFood("Burger")
customer.deleteFood("Salad")

print("Current order:", customer.order)