# Не дуже зрозумів завдання, тому зробив декілька варіантів.
# Чи є серед них вірний?)))

"""Creating a function, which takes in a country's name and capital as parameters.
Then creating a dictionary from those two, with 'name' as a key and 'capital' as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.

"""


def make_country(country, capital):
    info = {'country': country, 'capital': capital}
    return info


print(make_country('Ukraine', 'Kyiv'))


# Інший варіант

def make_country(**kwargs):
    return kwargs


print(make_country(country='Ukraine', capital='Kyiv'))


# Ще варіант

country = str(input('Print a country: '))
capital = str(input("Print it's capital: "))

def make_country(**kwargs):
    return kwargs


print(make_country(country=country, capital=capital))


# І ще один
def make_country(**kwargs):
    for key, value in kwargs.items():
        kwargs = dict(kwargs)
        return kwargs


print(make_country(country='Ukraine', capital='Kyiv'))
