# Name:Lane Sherrill
# Date: June 20, 2017

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

pdrome= raw_input("Type what the word you want: ")

plist=[]

for letter in pdrome:
    plist.append(letter)

lplist= len(plist)

for x in range(0,lplist):
    wutfir= plist[1:]
    wutlas= plist [:-1]
    wutbot= plist[1:-1]
    first= plist[0]
    last= plist[(lplist-1)]






    #TEST COMMANDS
print ""
print lplist
print ""
print plist
print""
print wutfir
print""
print wutlas
print""
print wutbot
print""
print first
print ""
print last