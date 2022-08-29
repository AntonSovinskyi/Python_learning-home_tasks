string_ = input("Please, enter a string: ")
if len(string_) == 1:
    print('')
else:
    string_ = string_[:2] + string_[-2:]
    print(string_)
