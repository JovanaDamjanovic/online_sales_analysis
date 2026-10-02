
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total_value(self):
        total = 0

        for product in self.cart_items:
            total += product.price * product.quantity

        return total

    def show_cart(self):
        print("Shopping cart:")

        for product in self.cart_items:
            product.display_info()
