"""Write a class Product"""


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.cash = 0
        self.products = {}

    # adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
    def add(self, product, amount):
        product.price = product.price * 1.3
        self.products[product] = amount

    # adds a discount for all products specified by input identifiers (type or name).
    # The discount must be specified in percentage
    def set_discount(self, identifier, percent, identifier_type='name'):
        for product in self.products:
            if identifier_type == 'name':
                if product.name == identifier:
                    product.price = product.price * (1 - percent / 100)
                else:
                    print('There is no such product')
            elif identifier_type == 'type':
                if product.type == identifier:
                    product.price = product.price * (1 - percent / 100)
                else:
                    print('There is no such product')
            else:
                print('Wrong identifier type')

    # removes a particular amount of products from the store if available, in other case raises an error.
    # It also increments income if the sell_product method succeeds.
    def sell_product(self, product_name, amount):
        for el in self.products:
            if el.name == product_name:
                if self.products[el] < amount:
                    raise Exception("We don't have enough stock")
                else:
                    self.products[el] -= amount
                    self.cash += el.price * amount

    # returns amount of many earned by ProductStore instance.
    def get_income(self):
        print(self.cash)
        return self.cash

    # returns information about all available products in the store.
    def get_all_products(self):
        print(self.products)
        return self.products

    # returns a tuple with product name and amount of items in the store.
    def get_product_info(self, product_name):
        for el in self.products:
            if el.name == product_name:
                print(el, self.products[el])
                break


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
