#PIG GAME

import random

psum = 0 #player score total
csum = 0 #computer score total
pturn = 0 #player turn total
cturn = 0 #computer turn total
turn = 'p' #whose turn it is (player goes first)
r = 0

while psum < 100 and csum < 100:
    if turn == 'p':
        if pturn == 0: #greets the player on their first roll of each turn
            print("It's your turn. The score is You:", psum, "Computer:", csum)
        r = random.randint(1,6)
        print("You rolled a", r)
        if r == 1:
            print("Sorry, no points this turn. Press Enter to switch to the computer's turn \n")
            input()
            pturn = 0
            turn = 'c' #no points if 1 is rolled, switches turn to computer
        elif r != 1:
            pturn += r #if 2-6 is rolled, adds that to turn total
            print("Your turn total is", pturn)
            re = input("Would you like to roll again? (Press Enter or r to reroll or type h to hold)") 
            if re == 'h': #if they choose not to reroll, the turn total is added to their game total
                psum += pturn
                print("Holding... Press Enter to switch to the computer's turn. \n")
                input()
                turn = 'c'
                print("Your game total is", psum, "\n")
                pturn = 0 #turn total resets after their turn
            elif re == 'r':
                print("Rerolling... \n") #rerolling does not change it to the computer's turn so the loop continues
                continue
            else:
                print("Rerolling... \n") #can press enter to reroll
                
    elif turn == 'c':
        print("___________________________________________________________________\n")
        print("It is the computer's turn. The computer's current score is", csum)
        while cturn < 20 and turn == 'c': #only rolls until 20 points are scored
            r = random.randint(1,6)
#            print("The computer rolled a", r)
            if r == 1:
#                print("The computer scored no points this turn.") #rolling a 1 switches back to player
                turn = 'p'
                cturn = 0 #turn total resets after computer's turn
            elif r != 1:
                cturn += r #adds roll to total if 2-6
#                print("The computer's turn total is", cturn)
                if cturn + csum >= 100: #if <20 points are needed to win this will skip to a computer victory
                    break
    
        csum += cturn #if more than 20 points are scored, adds points to total and switches to player
        turn = 'p'
        print("The computer scored", cturn, "points this turn.")
        print("The computer has scored", csum, "this game.")
        print("___________________________________________________________________ \n")
        cturn = 0 #turn total resets

if psum >= 100:
    print("CONGRATULATIONS! YOU WIN! Your final score was", psum)
elif csum >= 100:
    print("Sorry, you lost! The final score was You:", psum, "Computer:", csum)
