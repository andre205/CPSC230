#Pig Latin

vowels = ['a','e','i','o','u']

#easier to use an extra function to apply to both names
def pig(w):
    #get rid of uppercase so they dont get in the way
    w = w.lower()
    pigw = ''
    #make word a list so accessing each letter is easier
    lw = list(w)
    if lw[0] in vowels:
        #if first letter is a vowel, pigword is just normal word + yay
       pigw += w + 'yay'
    elif lw[0] not in vowels:
        #note the first letter and get rid of it
        fletter = lw[0]
        lw.remove(fletter)
        #make the list back into a string
        for i in range(len(lw)):
            pigw += lw[i]
        #add back on the first letter as well as ay
        pigw += fletter + 'ay'          
    return pigw

def nameToPig(f,l):
    return [pig(f),pig(l)]

print(nameToPig("Tyler","Andrews"))
print(nameToPig("Barrack","Obama"))
