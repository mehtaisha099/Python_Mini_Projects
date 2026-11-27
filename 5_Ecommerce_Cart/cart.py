cart = []

while True:
    print("\n--- E-commerce Cart ---")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))

        if product.strip() == "" or price <= 0:
            print("Invalid product or price.")
        else:
            cart.append([product, price])
            print("Product added successfully.")

    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            for i, item in enumerate(cart, 1):
                print(i, ".", item[0], "-", item[1])

    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            for i, item in enumerate(cart, 1):
                print(i, ".", item[0], "-", item[1])

            number = int(input("Enter product number to remove: "))

            if number >= 1 and number <= len(cart):
                cart.pop(number - 1)
                print("Product removed successfully.")
            else:
                print("Invalid product number.")

    elif choice == "4":
        total = 0

        for item in cart:
            total += item[1]

        print("Total Amount:", total)

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")