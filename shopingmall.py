class shop:
    shoppingmall = 'will not go'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #cart is a instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = shop('mehjabeen')
mehjabeen.add_to_cart('phone')
mehjabeen.add_to_cart('dress')
print(mehjabeen.cart)

nisho = shop('nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)