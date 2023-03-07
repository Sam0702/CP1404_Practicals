import random;

print("(G)et a valid score (must be 0-100 inclusive)")
print("(P)rint result")
print("(S)how stars")
print("(Q)uit")

choice = input("Enter your choice: ")

while choice != "Q":
    if choice == "G":
        print(random.randint(0, 100));

    elif choice == "P":
