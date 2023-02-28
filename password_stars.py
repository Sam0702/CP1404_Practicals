min_len = 10;

user = input("Enter a password: ")

while len(user) < min_len:
    print("The password need to have at least " + str(min_len) + " characters")
    user = input("Please enter a password: ")

print("*"*len(user))