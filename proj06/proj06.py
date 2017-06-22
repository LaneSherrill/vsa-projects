# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here

new_list=[]
def intersection (listc,word):
    winfactor=0
    newlength=len(listc)
    for item in word:
        new_list.append(item)
        newlength=newlength-1
        #if newlength==0:


def hangman():
    indexnum=0
    counter=0
    listc=[]
    wronglist=[]
    alphalist= ["a","b","c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print "Welcome to hangman"
    #word=choose_word(wordlist)
    word = list(choose_word(wordlist))
    #print word
    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    num_guess=len(word)
    length=len(word)
    LIST = [len(word) * "_ "]  #####
    print "The word is", length,"letters long. You have", length, "guesses."
    for x in range(0,int(length)): #**********
                 listc.append("_ ")
    while num_guess!=0:
                guess = raw_input("Guess a letter: ")
                print ""
                if guess in alphalist:
                    if guess in word:
                        print guess,"is in this word."
                        #listc.append(guess)
                        #print listc
                        if listc == word:
                            print "correct letters=", listc
                            print "wrong letters=", wronglist
                            intersection(listc, word)
                       #WHERE THE LETTER IS LOCATED, CODE  (INC)
                        for num in range(0,len(word)):
                            indexnum=num
                            #print indexnum
                            # If statement isnt working
                            #print listc[indexnum]
                            #print word[indexnum]
                            if guess == word[indexnum]:
                                    listc[indexnum]=guess
                        #print "listc =",listc




                    elif guess in listc:
                        print "You already guessed this. Please guess again."
                    elif guess in wronglist:
                        print "You already guessed this. Please guess again"
                    else:
                        print guess, "was not correct."
                        wronglist.append(guess)
                        num_guess=num_guess-1
                else:
                    print "Your guess was either capitalized, more than one letter, or it is not in the alphabet. Guess again."

                if num_guess==0:
                    print ""
                    print "YOU RAN OUT OF GUESSES"
                    print" "
                    print "The correct word was", word
                    print ""
                    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                    break
                print "correct letters=", listc
                print "wrong letters=", wronglist
                print "You have", num_guess, "guesses left."
                print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                if listc==word:
                    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                    print"  Y                   "
                    print"      O                   "
                    print"          U                   "
                    print"  W                   "
                    print"      O                   "
                    print"          N                   "
                    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                    break
hangman()


#for guess in word:
                           #counter=counter+1
                            #if counter>2 or counter==2:
                                #print guess,"is in the word multiple times."
                                #listc.append(guess)
                                #print listc
                            #counter=0