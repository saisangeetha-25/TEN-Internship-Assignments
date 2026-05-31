# =====================================
# SMART INVENTORY MANAGEMENT SYSTEM
# =====================================

inventory = {}
categories = set()

# -------------------------------------
# Add Product
# -------------------------------------
def add_product():

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Product ID already exists!")
        return

    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier Name: ")

    inventory[product_id] = {
        "name": product_name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "supplier": supplier
    }

    categories.add(category)

    print("Product Added Successfully!")


# -------------------------------------
# Update Inventory
# -------------------------------------
def update_inventory():

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product Not Found!")
        return

    print("1. Update Quantity")
    print("2. Update Price")

    choice = input("Enter choice: ")

    if choice == "1":

        new_quantity = int(input("Enter New Quantity: "))
        inventory[product_id]["quantity"] = new_quantity

    elif choice == "2":

        new_price = float(input("Enter New Price: "))
        inventory[product_id]["price"] = new_price

    else:
        print("Invalid Choice")
        return

    print("Inventory Updated Successfully!")


# -------------------------------------
# Search Product
# -------------------------------------
def search_product():

    search_value = input(
        "Enter Product ID or Product Name: "
    ).lower()

    found = False

    for product_id, product in inventory.items():

        if (
            product_id.lower() == search_value
            or product["name"].lower() == search_value
        ):

            print("\nProduct Found")
            print(product_id, product)

            found = True

    if not found:
        print("Product Not Found")


# -------------------------------------
# Display Inventory
# -------------------------------------
def display_inventory():

    if len(inventory) == 0:
        print("Inventory Empty")
        return

    print("\n========== INVENTORY ==========")

    print(
        f"{'ID':<10}"
        f"{'NAME':<15}"
        f"{'CATEGORY':<15}"
        f"{'QTY':<10}"
        f"{'PRICE':<10}"
        f"{'SUPPLIER':<15}"
    )

    for product_id, product in inventory.items():

        print(
            f"{product_id:<10}"
            f"{product['name']:<15}"
            f"{product['category']:<15}"
            f"{product['quantity']:<10}"
            f"{product['price']:<10}"
            f"{product['supplier']:<15}"
        )


# -------------------------------------
# Out Of Stock Alert
# -------------------------------------
def out_of_stock_alert():

    print("\nOut Of Stock Products")

    found = False

    for product_id, product in inventory.items():

        if product["quantity"] == 0:

            print(product_id, "-", product["name"])

            found = True

    if not found:
        print("No Out Of Stock Products")


# -------------------------------------
# Low Stock Alert
# -------------------------------------
def low_stock_alert():

    threshold = int(
        input("Enter Low Stock Threshold: ")
    )

    print("\nLow Stock Products")

    found = False

    for product_id, product in inventory.items():

        if product["quantity"] < threshold:

            print(
                product_id,
                "-",
                product["name"],
                "Qty:",
                product["quantity"]
            )

            found = True

    if not found:
        print("No Low Stock Products")


# -------------------------------------
# Inventory Report
# -------------------------------------
def inventory_report():

    total_items = 0
    total_value = 0

    category_summary = {}

    for product in inventory.values():

        total_items += product["quantity"]

        total_value += (
            product["quantity"]
            * product["price"]
        )

        category = product["category"]

        if category not in category_summary:
            category_summary[category] = 0

        category_summary[category] += product["quantity"]

    print("\n========== REPORT ==========")

    print("Total Items :", total_items)

    print("Total Inventory Value :",
          round(total_value, 2))

    print("\nCategory Wise Summary")

    for category, count in category_summary.items():

        print(category, ":", count)
# -------------------------------------
# Delete Product
# -------------------------------------
def delete_product():
    product_id = input(
        "Enter Product ID to Delete: "
    )
    if product_id in inventory:
        del inventory[product_id]
        print("Product Deleted Successfully")
    else:
        print("Product Not Found")
# -------------------------------------
# Show Categories
# -------------------------------------
def show_categories():

    print("\nProduct Categories")

    for category in categories:
        print(category)

# Main Menu
# -------------------------------------
while True:

    print("\n===== SMART INVENTORY SYSTEM =====")

    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Out Of Stock Alert")
    print("6. Category Management")
    print("7. Inventory Report")
    print("8. Delete Product")
    print("9. Low Stock Alert")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        out_of_stock_alert()
    elif choice == "6":
        show_categories()
    elif choice == "7":
        inventory_report()
    elif choice == "8":
        delete_product()
    elif choice == "9":
        low_stock_alert()
    elif choice == "10":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")