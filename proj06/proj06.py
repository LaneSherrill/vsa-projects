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
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #print "  ", len(wordlist), "words loaded."
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


def hangmanart(num_guess, word):
    if num_guess == len(word):
        print '       0000000000000000000000     '
        print '       0                         '
        print '       0                      '
        print '       0                     '
        print '       0                      '
        print '       0                         '
        print '       0                      '
        print '       0                      '
        print '       0                      '
        print '       0                      '
        print '       0                      '
        print '       0                        '
        print '       0                        '
        print '       0                        '
        print '       0                    '
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

    if num_guess == len(word) - 1:
        print '       0000000000000000000000     '
        print '       0                    0     '
        print '       0                   111    '
        print '       0                  1o1o1   '
        print '       0                   111    '
        print '       0                         '
        print '       0                      '
        print '       0                      '
        print '       0                      '
        print '       0                      '
        print '       0                      '
        print '       0                        '
        print '       0                        '
        print '       0                        '
        print '       0                    '
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

    if num_guess == len(word) - 2:
        print '       0000000000000000000000     '
        print '       0                    0     '
        print '       0                   111    '
        print '       0                  1o1o1   '
        print '       0                   111    '
        print '       0                    1     '
        print '       0                   111    '
        print '       0                   222   '
        print '       0                   222   '
        print '       0                   222   '
        print '       0                   222   '
        print '       0                        '
        print '       0                        '
        print '       0                        '
        print '       0                    '
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

    if num_guess == len(word) / 2:
        print '       0000000000000000000000     '
        print '       0                    0     '
        print '       0                   111    '
        print '       0                  1o1o1   '
        print '       0                   111    '
        print '       0                    1     '
        print '       0                   111    '
        print '       0                  1222   '
        print '       0                 1 222   '
        print '       0                1  222   '
        print '       0                1  222   '
        print '       0                        '
        print '       0                        '
        print '       0                        '
        print '       0                    '
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

    if num_guess == len(word) / 2 - 1:
        print '       0000000000000000000000     '
        print '       0                    0     '
        print '       0                   111    '
        print '       0                  1o1o1   '
        print '       0                   111    '
        print '       0                    1     '
        print '       0                   111    '
        print '       0                  12221   '
        print '       0                 1 222 1  '
        print '       0                1  222  1 '
        print '       0                1  222  1 '
        print '       0                        '
        print '       0                        '
        print '       0                        '
        print '       0                    '
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

    if num_guess == len(word) / 2 - 2:
        print '       0000000000000000000000     '
        print '       0                    0     '
        print '       0                   111    '
        print '       0                  1o1o1   '
        print '       0                   111    '
        print '       0                    1     '
        print '       0                   111    '
        print '       0                  12221   '
        print '       0                 1 222 1  '
        print '       0                1  222  1 '
        print '       0                1  222  1 '
        print '       0                   1     '
        print '       0                  1      '
        print '       0                  1      '
        print '       0                111    '
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

    if num_guess == 0:
        print '       0000000000000000000000     '
        print '       0                    0     '
        print '       0                   111    '
        print '       0                  1o1o1   '
        print '       0                   111    '
        print '       0                    1     '
        print '       0                   111    '
        print '       0                  12221   '
        print '       0                 1 222 1  '
        print '       0                1  222  1 '
        print '       0                1  222  1 '
        print '       0                   1 1    '
        print '       0                  1   1   '
        print '       0                  1   1   '
        print '       0                111    111'
        print '       0                          '
        print '       0                          '
        print '       0                          '
        print '000000000000000                   '

def hangman():
    indexnum=0
    counter=0
    listc=[]
    wronglist=[]
    alphalist= ["a","b","c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print ""
    print "Welcome to hangman"
    print ""
    word = list(choose_word(wordlist))
    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    num_guess=len(word)
    length=len(word)
    LIST = [len(word) * "_ "]
    if len(word)<=6:
        print "The word is pretty easy and its only", length,"letters long. You have", length, "guesses."
    elif 6<len(word)<8:
        print "This is a medium difficulty word and only", length,"letters long. You have", length, "guesses."
    elif 8<=len(word):
        print "The word is very difficult and its", length,"letters long. You have", length, "guesses."
    for x in range(0,int(length)):
                 listc.append("_ ")
    while num_guess!=0:
                guess = raw_input("Guess a letter: ")
                print ""
                if guess in alphalist:
                    if guess in word:
                        print guess,"is in this word."
                        if listc == word:
                            print "correct letters=", listc
                            print "wrong letters=", wronglist
                            intersection(listc, word)
                        for num in range(0,len(word)):
                            indexnum=num
                            if guess == word[indexnum]:
                                    listc[indexnum]=guess
                    elif guess in listc:
                        print "You already guessed this. Please guess again."
                    elif guess in wronglist:
                        print "You already guessed this. Please guess again"
                    else:
                        print guess, "was not correct."
                        wronglist.append(guess)
                        num_guess=num_guess-1
                        hangmanart(num_guess, word)
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
                    print"  Y   o   u       W   o   n           Y   o   u       W   o   n          "
                    print"  Y   o   u       W   o   n           Y   o   u       W   o   n              "
                    print"  Y   o   u       W   o   n           Y   o   u       W   o   n                  "
                    print"  Y   o   u       W   o   n           Y   o   u       W   o   n          "
                    print"  Y   o   u       W   o   n           Y   o   u       W   o   n              "
                    print"  Y   o   u       W   o   n           Y   o   u       W   o   n                  "
                    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                    break

hangman()


























