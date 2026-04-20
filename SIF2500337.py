#Food Ordering System

print("MENU")

print("1. Burger - 500")

print("2. Pizza - 1000")

print("3. Juice - 300")

print("4. Sandwich - 400")

choice = input("Enter your choice (burger/pizza/juice): ").lower()

quantity = int(input("Enter quantity: "))

if choice == "burger":

    price = 500

elif choice == "pizza":

    price = 1000

elif choice == "juice":

    price = 300

elif choice == "sandwich":

    price = 400

else:

    print("Wrong Selection Try Again!")

    exit()


total = price * quantity


print("You ordered:", choice)

print("Quantity:", quantity)

print("Total bill:", total)
