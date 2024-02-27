
#Main Method
def main():



    prices = {

        "Pizza" : 13.99,
        "Fries" : 2.99,
        "Wings" : 3.99

    }

    dummyOrder = {
        "Pizza" : 1,
        "Fries" : 3,
        "Wings" : 2
    }

    ReviewReceipts(dummyOrder,prices)

#Print Recept
def ReviewReceipts(order, prices):

    priceHolder = 0
    subTotal = 0
    print("             Pizza House        ")
    print("---------------------------------")
    print("             Order Summary       ")
    print("Item          Quantity          Price\n")

    for orderItem in order:
        priceHolder = order[orderItem] * prices[orderItem]

        print(orderItem + "          " + str(order[orderItem]) + "          $" + str(priceHolder))

        subTotal += priceHolder

    print("\nSubtotal:                    $" + str(subTotal))

#Call Main
main()
