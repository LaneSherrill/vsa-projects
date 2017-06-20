# Name: Lane Sherrill
# Date: June 20, 2017


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random

rdnum= random.randint(1, 9)

print ""
print "The high/low feature was too buggy for me to fix so i left it out, sorry."
print ""
print ""
gsnum = raw_input("     Guess a number between 1 and 9. You only have 5 guesses: ")


numofgus= 3
loss=0

if int(gsnum) == int(rdnum):
    if 0<rdnum<2:
        print "Correct!"
    elif 2<rdnum<6:
        print "Good job, you got it!"
    elif 6<rdnum:
        print "Congrats, you guessed right!"
    exitcmmd = raw_input("Type exit to quit the game: ")

else:
    print " "
    print " 4 more guesses"
    print " "
    gsnum= raw_input("     Guess again: ")
    print " "
    print " 3 more guesses"
    print " "

while int(gsnum)!= int(rdnum):

    while loss> -1:

        if numofgus==0:
                print " y "
                print "     o"
                print "         u"
                print "             "

                print "                 l"
                print "                     o"
                print "                         s"
                print "                             e"
                loss=numofgus-1
                numofgus=loss

        else:
                gsnum=raw_input("   Guess again: ")
                chancesleft=numofgus-1
                numofgus=chancesleft
                print " "
                print " ",numofgus, " more guesses"
                print " "
