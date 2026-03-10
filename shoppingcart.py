cart = {}

def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    if item in cart:
        cart[item]["qty"] += qty
    else:
        cart[item] = {"price": price, "qty": qty}

def remove_item():
    item = input("Enter item name to remove: ")
    if item in cart:
        del cart[item]
    else:
        print("Item not found")

def view_cart():
    if not cart:
        print("Cart is empty")
        return
    total = 0
    for item, data in cart.items():
        subtotal = data["price"] * data["qty"]
        total += subtotal
        print(item, "-", data["qty"], "x", data["price"], "=", subtotal)
    print("Total:", total)

def checkout():
    view_cart()
    print("Checkout complete")
    cart.clear()

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        break
    else:
        print("Invalid choice")