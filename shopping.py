class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item ['quantity']
        print('total price:',total)
        if amount < total:
            print(f'please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'here is your items and money {extra}')


abd = shopping('bbdur rahman')
abd.add_to_cart('potato',50,2)
abd.add_to_cart('tomato',70,2)
print(abd.cart)
abd.checkout(1000)
