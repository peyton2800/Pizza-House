
#Main Method
def main():
    loopMenu = True

    #Temp Menu for testing
    restarauntMenu = ["Pizza", "Fries", "Wings"]

    while(loopMenu):
        print("Menu Add/Remove program")
        userChoice = input("1 - Menu , 2 - Add item , 3 - Remove Item\n")

        if(userChoice == "1"):
            Menu(restarauntMenu)
        elif (userChoice == "2"):
            addItem(restarauntMenu)
        elif (userChoice == "3"):
            deleteItem(restarauntMenu)
        else:
            print("Invalid Option, pleaes try again!\n")


#Display Menu Items
def Menu(restarauntMenu):

    print("Pizza House Menu")
    print("-----------------------")

    for Item in restarauntMenu:
        print(Item)
    print ("\n")

#Add an Item to Menu
def addItem(restarauntMenu):
    newItem = input("What Item do you want to add to the Menu?\n")
    restarauntMenu.append(newItem)
    print(newItem + " Added to the Menu\n")

#Delete an Item from the menu
def deleteItem(restarauntMenu):
    Menu(restarauntMenu)
    removeItem = input("What Item do you want to remove from the Menu?\n")

    try:
        restarauntMenu.remove(removeItem)
        print(removeItem + " Removed from the menu\n")
    except:
        print(removeItem + " is not in the list!\n")

#Call Main
main()
