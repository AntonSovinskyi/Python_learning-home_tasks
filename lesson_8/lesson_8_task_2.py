"""Creating a function, which takes in a country's name and capital as parameters.
Then creating a dictionary from those two, with 'name' as a key and 'capital' as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.

"""


def make_country(country, capital):
    info = {'country': country, 'capital': capital}
    return info


print(make_country('Ukraine', 'Kyiv'))
