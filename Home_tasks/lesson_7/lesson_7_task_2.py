"""Compute the total price of the stock where the total price

is the sum of the price of an item multiplied by the quantity of this exact item.


"""


from numpy import multiply


stock = {'banana': 6, 'apple': 0, 'orange': 32, 'pear': 15}
prices = {'banana': 4, 'apple': 2, 'orange': 1.5, 'pear': 3}

stock_list = []
prices_list = []

for amount in stock.values():
    stock_list.append(amount)

for price in prices.values():
    prices_list.append(price)

print(f'Total price:', sum(multiply(stock_list, prices_list)))
