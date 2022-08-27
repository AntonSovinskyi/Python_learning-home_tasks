while True:
    city = input('Print city: ')
    if city == 'exit':
        break
        print(city.upper())
    elif city:
        print(city.upper())
    elif city == ' ':
        pass
