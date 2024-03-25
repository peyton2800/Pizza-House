def leave_review():
    # Initializs a empty dictionary to store reviews
     reviews = {}

    # Prompt  user for their name
    user_name = input("Please enter your name: ")

    # Prompt to user for their review
   user_review = input("Please leave your review of the restaurant and your experience: ")

    # Prompt user for their rating
     user_rating = int(input("Please rate your experience (from 1 to 5): "))
    while user_rating < 1 or user_rating > 5:
        user_rating = int(input("Invalid rating! Please rate your experience from 1 to 5: "))

    # Store review and rating in the dictionary
    reviews[user_name] = [user_review, user_rating]

    # Display the confirmation message
    print("Thank you for your review!")

    return reviews