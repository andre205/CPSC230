string = input("Enter a string to shift ")
shift = input("Enter a number to shift by ")

def cipher(s, shift):
    output = ""
    for i in range(len(s)):
        add = ord(string[i]) + shift
        output += add
    return output

print(shift(string, shift))
