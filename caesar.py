def alphabet_position(letter):
    high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    if letter in high:
        return high.index(letter)
    if letter in low:
        return low.index(letter)

def rotate_character(char, rot):
    high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    pos = alphabet_position(char)
    if char in high:
        return high[(pos+rot) % 26]
    if char in low:
        return low[(pos+rot) % 26]
    else:
        return char

def encrypt(text, rot):
    newword = ""
    for char in text:
        newword+= rotate_character(char, rot)
    return newword
