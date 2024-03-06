# UserRegistrationForm
# Chris Dixon
# 03/06/2024

"""User account"""
# NewUser dictionary
NewUser = {}

# user_account dictionary
user_account = {}

# user_List list
user_List = []


# Input information
def account_registration():
    while True:
        NewUser = {}
        user_account = {}
        if not user_List:
            print(f"\n[List empty]\n")
        elif user_List:
            print(f"User list: \n{user_List}\n")

        # Username
        NewUser['name'] = input("what is your name? ")
        if NewUser['name'] not in NewUser and NewUser['name'] not in user_List:
            user_account["name"] = NewUser['name']
        elif NewUser['name'] in user_List:
            print(f"User: \n{NewUser['name']} already added. Please try another.")
        else:
            print("Invalid")

        # email
        NewUser['email'] = input("what is your email? ")
        if NewUser['email'] not in NewUser and NewUser['email'] not in user_List:
            user_account["email"] = NewUser['email']
        elif NewUser['email'] in user_List:
            print(f"User: \n{NewUser['email']} already added. Please try another.")
        else:
            print("Invalid")

        # phone
        NewUser['phonenumber'] = input("what is your phone number? ")
        if NewUser['email'] not in NewUser and NewUser['email'] not in user_List:
            user_account["phonenumber"] = NewUser['phonenumber']
        elif NewUser['phonenumber'] in user_List:
            print(f"User: \n{NewUser['phonenumber']} already added. Please try another.")
        else:
            print("Invalid")

        # address
        NewUser['address'] = input("what is your address? ")
        if NewUser['address'] not in user_List:
            user_account["address"] = NewUser['address']
        else:
            print("Invalid")

        # city
        NewUser['city'] = input("what is your city? ")
        if NewUser['city'] not in user_List:
            user_account["city"] = NewUser['city']
        else:
            print("Invalid")

        # state
        NewUser['state'] = input("what is your state? ")
        if NewUser['state'] not in user_List:
            user_account["state"] = NewUser['state']
        else:
            print("Invalid")

        # country
        NewUser['country'] = input("what is your country? ")
        if NewUser['country'] not in user_List:
            user_account["country"] = NewUser['country']
        else:
            print("Invalid")

        # zip
        NewUser['zip'] = input("what is your zip code? ")
        if NewUser['zip'] not in user_List:
            user_account["zip"] = NewUser['zip']
        else:
            print("Invalid")
        break

    user_List.append(user_account)


account_registration()
print(f"\nWelcome, {user_account['name']}.\n")

print(f"User account: \n{user_account}\n")
print(f"User list: \n{user_List}\n")

choice = input(f"Would you like to register a new user account? Y/n \n")
if choice == "Y":
    account_registration()
elif choice == "n":
    quit("End")
