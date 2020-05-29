"""
    Cezar z dowolnym przesunięciem.
"""


def caesar(text, shift):
    alphabet = ""
    code = ""

    for a in range(65, 91):  # 65 - A, 90 - Z
        alphabet += chr(a)

    size = len(alphabet)

    for char in text:
        if char.isupper():
            pos = (alphabet.index(char) + shift) % size
            code += alphabet[pos]
        elif char.islower():
            pos = (alphabet.index(char.upper()) + shift) % size
            code += alphabet[pos].lower()
        else:
            code += char

    return code


str = "THIS IS some SECRET INFORMATION :)"
shift = 13
print(f"To code: {str}")
coded = caesar(str, shift)
print(f"Coded: {coded}")
