def alphabet_position(letter):
    """receives a letter (that is, a string with only one alphabetic character)"""
    """and returns the 0-based numerical position of that letter"""
    """within the alphabet."""

    letter = letter.upper()
    position = ord(letter) - 65
    return position

def rotate_character(char, rot):
    """receives a character char (that is, a string of length 1),"""
    """and an integer rot. Your function should return a new string of length 1,"""
    """ the result of rotating char by rot number of places to the right."""
    newchar = ""
    if char.isalpha():
        position = alphabet_position(char)
        if position + rot <= 25:
            newposition = position + rot
        else:
            newposition = (position + rot) % 26
        newchar = chr(newposition+65)
        if char.islower():
            newchar = newchar.lower()
        else:
            newchar = newchar.upper()
    else:
        newchar = char
    return newchar

def encrypt(text, rot):
    rot = rot
    newtext = ""
    for char in text:
        newchar = rotate_character(char, rot)
        newtext += newchar
    return newtext
