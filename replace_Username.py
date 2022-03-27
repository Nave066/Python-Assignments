# Replacing the string with username input from user
print("Hello <<username>>, How are you?")  # Original string
user_input = input("Enter Your Username here -->")
if len(user_input) >= 3:
    print("Hello " + user_input + ", How are you?")  # replaced string
else:
    print("Sorry, Your Username must contain Minimum 3 character")
