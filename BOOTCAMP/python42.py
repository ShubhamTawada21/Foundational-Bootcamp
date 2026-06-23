class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

product_data = [
    ("Laptop", 999.99, 5),
    ("Mouse", 24.99, 15),
    ("Keyboard", 49.99, 10)
]

products_list = []
for name, price, quantity in product_data:
    product_obj = Product(name, price, quantity)
    products_list.append(product_obj)

grand_total = 0
for product in products_list:
    value = product.total_value()
    grand_total += value
    print(f"Product: {product.name} | Total Value: ${value:.2f}")

print("-" * 30)
print(f"Grand Total Inventory Value: ${grand_total:.2f}")