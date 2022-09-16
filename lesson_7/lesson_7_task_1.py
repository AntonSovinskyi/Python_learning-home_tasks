"""Make a program that has some sentence (a string) on input

 and returns a dict containing all unique words as keys and
 the number of occurrences as values.

 """


text_ = 'While The Python Language Reference describes the exact syntax and semantics \
of the Python language, this library reference manual describes the standard library that \
is distributed with Python. It also describes some of the optional components that are \
commonly included in Python distributions.'

text_1 = text_.split()
text_2 = set(text_1)

unique_words = {}

if len(text_1) == len(text_2):
    print('No matches found.')
elif len(text_1) != len(text_2):
    print('Matches are found.')

for el in text_1:
    unique_words[el] = text_1.count(el)

print(unique_words)

