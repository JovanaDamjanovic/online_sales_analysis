
import random

from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

product1 = Product("Laptop", 1000, 3)
product2 = Product("Phone", 500, 6)
product3 = Product("Mouse", 25, 10)
product4 = Product("Keyboard", 50, 4)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)

print("Available products:")
manager.show_products()

print("Total inventory value:", manager.total_value())

cart = Cart()

selected_products = random.sample(manager.products, 3)

for product in selected_products:
    cart.add_product(product)

cart.show_cart()

print("Total cart value:", cart.total_value())
