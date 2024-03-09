#Main Method

def main():

    #Temp Order
    Order = {
        "Cheese Pizza" : 1,
        "BBQ Wings" : 3,
        "Sprite" : 2
    }

    #Temp Ratings
    Ratings = {
        "Cheese Pizza" : 4,
        "Pepperoni Pizza" : 4,
        "Sausage Pizza" : 3,
        "Plain Wings" : 4,
        "BBQ Wings" : 5,
        "Breadsticks" : 5,
        "Cheesesticks" : 4,
        "Pepsi" : 4,
        "Water" : 5,
        "Sprite" : 3

    }

    #Call Rate Functions
    userRatings = rate(Order)

    #sort dict
    Ratings = dict(sorted(Ratings.items(), key=lambda item: item[1], reverse=True))

    print("\nTop Rated Menu Items\n-------------")
    for item in Ratings:
        print(item + " with a Rating of: " + str(Ratings[item]) + " stars")


def rate(order):
    ratings = {}
    userRate = 0
    for item in order:
        loopRating = True

        while(loopRating):
            try:
                userRate = int(input("Please rate " + item + " out of 5 stars "))
                if (userRate > 5) or (userRate < 1) :
                    print("Invalid, please enter a number between 1-5")
                else:
                    ratings[item] = userRate
                    loopRating = False
            except:
                 print("Non-Number Entered")

    return ratings



#Call main
main()
