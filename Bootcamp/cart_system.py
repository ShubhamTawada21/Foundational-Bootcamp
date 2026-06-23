products = {
    "1": {"name": "Laptop", "price": 799.99},
    "2": {"name": "Smartphone", "price": 499.99},
    "3": {"name": "Headphones", "price": 89.99},
    "4": {"name": "Keyboard", "price": 49.99},
}

cart = {}


def display_catalog():
    print("\n=== DIGITAL SHOPPING CART ===")
    print("Available products:")
    for code, item in products.items():
        print(f"{code}. {item['name']} - ${item['price']:.2f}")


def display_cart():
    print("\n--- Your Cart ---")
    if not cart:
        print("Your cart is empty.")
        return

    total = 0
    for code, item in cart.items():
        product = products[code]
        line_total = product["price"] * item["quantity"]
        total += line_total
        print(f"{product['name']} x{item['quantity']} = ${line_total:.2f}")

    print(f"Total: ${total:.2f}")


def add_to_cart():
    display_catalog()
    code = input("Enter product number to add (or 0 to cancel): ").strip()

    if code == "0":
        print("No item added.")
        return

    if code not in products:
        print("Invalid product number.")
        return

    try:
        quantity = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if code in cart:
        cart[code]["quantity"] += quantity
    else:
        cart[code] = {"quantity": quantity}

    product_name = products[code]["name"]
    print(f"Added {quantity} x {product_name} to your cart.")


def remove_from_cart():
    if not cart:
        print("Your cart is empty.")
        return

    print("\nItems in your cart:")
    for code, item in cart.items():
        print(f"{code}. {products[code]['name']} x{item['quantity']}")

    code = input("Enter product number to remove (or 0 to cancel): ").strip()
    if code == "0":
        return

    if code not in cart:
        print("That item is not in your cart.")
        return

    del cart[code]
    print(f"Removed {products[code]['name']} from your cart.")


def checkout():
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
        return

    total = 0
    print("\n--- Checkout Receipt ---")
    for code, item in cart.items():
        product = products[code]
        line_total = product["price"] * item["quantity"]
        total += line_total
        print(f"{product['name']} x{item['quantity']} = ${line_total:.2f}")

    print(f"Total amount due: ${total:.2f}")
    print("Thank you for shopping with us!")
    cart.clear()


while True:
    print("\n1. View products")
    print("2. Add item to cart")
    print("3. View cart")
    print("4. Remove item from cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        display_catalog()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        remove_from_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
