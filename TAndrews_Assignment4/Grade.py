#LetterGrade with nested ifs

g=input("What is your letter grade?")

if g.startswith('A'):
    if g.endswith('+'):
        print("Your GPA is 4.3")
    elif g.endswith('-'):
        print("Your GPA is 3.6")
    else: print("Your GPA is 4.0")
elif g.startswith('B'):
    if g.endswith('+'):
        print("Your GPA is 3.3")
    elif g.endswith('-'):
        print("Your GPA is 2.6")
    else: print("Your GPA is 3.0")
elif g.startswith('C'):
    if g.endswith('+'):
        print("Your GPA is 2.3")
    elif g.endswith('-'):
        print("Your GPA is 1.6")
    else: print("Your GPA is 2.0")
elif g.startswith('D'):
    if g.endswith('+'):
        print("Your GPA is 1.3")
    elif g.endswith('-'):
        print("Your GPA is .7")
    else: print("Your GPA is 1.0")
else: print("You are failing or input an incorrect letter grade.")
