#Complement and RevComplement of DNA Strings

valid = ['A','C','T','G']
#A-T
#G-C
inputting = True
error = 0

#Enter strings until no errors
while inputting:
    s = list(input("Enter a DNA string."))
    error = 0
    for i in range(len(s)):
        if not s[i] in valid:
            error += 1
    if error > 0:
        print("There is an error in your string")
        continue
    elif error == 0:
        break
#compose a new string by adding the comlement of each letter 1 by 1       
def complement(s):
    comp = ""
    for i in range(len(s)):
        if s[i] == 'A':
            comp += 'T'
        elif s[i] == 'T':
            comp += 'A'
        elif s[i] == 'G':
            comp += 'C'
        elif s[i] == 'C':
            comp += 'G'
    return comp

#flip it for revcomplement
def revComplement(s):
    c = complement(s)
    return c[::-1]

print(complement(s))
print(revComplement(s))
