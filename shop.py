class shop:
    cart = [] #cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

abrar = shop('abrar')
abrar.add_to_cart('shoes')
abrar.add_to_cart('mobile')
print(abrar.cart)

nisho = shop('nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)
