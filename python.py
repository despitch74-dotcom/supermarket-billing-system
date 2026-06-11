<<<<<<< HEAD
# SmartBuy Supermarket Billing System

while True:

    products = []
    quantities = []
    prices = []
    totals = []

    print("\n========== SMARTBUY SUPERMARKET ==========")

    num_products = int(input("Enter number of products purchased: "))

    subtotal = 0

    for i in range(num_products):

        print(f"\nProduct {i + 1}")

        product = input("Product Name: ")
        quantity = int(input("Quantity Purchased: "))
        price = float(input("Price per Unit (Le): "))

        total = quantity * price

        products.append(product)
        quantities.append(quantity)
        prices.append(price)
        totals.append(total)

        subtotal += total

    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_bill = subtotal - discount

    print("\n========================================")
    print("         SMARTBUY RECEIPT")
    print("========================================")

    print("{:<15}{:<10}{:<10}{:<10}".format(
        "Product", "Qty", "Price", "Total"))

    for i in range(num_products):
        print("{:<15}{:<10}{:<10}{:<10}".format(
            products[i],
            quantities[i],
            prices[i],
            totals[i]
        ))

    print("----------------------------------------")
    print(f"Subtotal: Le {subtotal:.2f}")
    print(f"Discount: Le {discount:.2f}")
    print(f"Amount Payable: Le {final_bill:.2f}")
    print("========================================")

    choice = input(
        "\nProcess another customer? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using SmartBuy Billing System.")
        break
=======
# SmartBuy Supermarket Billing System

while True:

    products = []
    quantities = []
    prices = []
    totals = []

    print("\n========== SMARTBUY SUPERMARKET ==========")

    num_products = int(input("Enter number of products purchased: "))

    subtotal = 0

    for i in range(num_products):

        print(f"\nProduct {i + 1}")

        product = input("Product Name: ")
        quantity = int(input("Quantity Purchased: "))
        price = float(input("Price per Unit (Le): "))

        total = quantity * price

        products.append(product)
        quantities.append(quantity)
        prices.append(price)
        totals.append(total)

        subtotal += total

    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_bill = subtotal - discount

    print("\n========================================")
    print("         SMARTBUY RECEIPT")
    print("========================================")

    print("{:<15}{:<10}{:<10}{:<10}".format(
        "Product", "Qty", "Price", "Total"))

    for i in range(num_products):
        print("{:<15}{:<10}{:<10}{:<10}".format(
            products[i],
            quantities[i],
            prices[i],
            totals[i]
        ))

    print("----------------------------------------")
    print(f"Subtotal: Le {subtotal:.2f}")
    print(f"Discount: Le {discount:.2f}")
    print(f"Amount Payable: Le {final_bill:.2f}")
    print("========================================")

    choice = input(
        "\nProcess another customer? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using SmartBuy Billing System.")
        break
>>>>>>> 2769ad544bc6ae84e3f8a918c7876cfd425d6f4f
