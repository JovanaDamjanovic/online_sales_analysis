

from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 1000, 3)
product2 = Product("Phone", 500, 7)
product3 = Product("Mouse", 25, 10)
product4 = Product("Keyboard", 50, 4)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)

