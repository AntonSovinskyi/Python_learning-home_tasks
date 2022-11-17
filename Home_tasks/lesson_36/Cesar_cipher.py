def Cesar_cipher(word):
    big_letter = [65, 90]
    small_letter = [97, 122]
    result = []
    count = 3
    for letter in word:
        if big_letter[0] <= ord(letter) <= big_letter[1]:
            position = ord(letter) + count
            if position <= big_letter[1]:
                result.append(chr(position))
            else:
                diff = position - big_letter[1] - 1
                result.append(chr(big_letter[0] + diff))
        elif small_letter[0] <= ord(letter) <= small_letter[1]:
            position = ord(letter) + count
            if position <= small_letter[1]:
                result.append(chr(position))
            else:
                diff = position - small_letter[1] - 1
                result.append(chr(small_letter[0] + diff))
    return ''.join(result)
