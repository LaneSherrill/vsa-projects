# REVIEW: Conditionals, for loops, lists, and functions

#INSTRUCTIONS:

#PartI:

#Make the string "sentence_string" into a list called "sentence_list"
#Use a for loop and an append function like this: list.append(something)
i=0
sentence_list=[]
sentence_string = raw_input("Type out a sentence and find all of the vowels in it: ")
#print sentence_list
for x in range(0,len(sentence_string)):
    sentence_list.append(sentence_string[i])
    i=i+1
#print sentence_list


#PartII:
# Print every item of the list using a for loop

i=0
for x in range(0,len(sentence_string)):
    #print sentence_list[i]
    i=i+1



#PartIII:
# write a for loop to find the index of 'b' in the list "vowels"
i=0
vowels = ['a', 'b', 'i', 'o', 'u', 'y',"A","E","I","O","U"]
for x in range(0,len(vowels)):
    if vowels[i]=='b':
        #print "The letter B is at index",i
        break
    else:
        i=i+1

#PartIV
# use the index found above to change 'b' to 'e'
for x in range(0,len(vowels)):
    if vowels[i]=='b':
        vowels[i]="e"
        #print vowels
        break



#PartV:
# Using a for statement and an if statement, print all the vowels from the sentence
i=0
for x in range(0,len(sentence_string)):
    if sentence_list[i] in vowels:
        #print sentence_list[i]
        i=i+1
    else:
        i=i+1


#PartVI:
#Make a new function called "vowelFinder" that will return a list that holds all the vowels found in a list (no duplicates).
#The function's parameters should be "list" and "vowels."
# """
# Example:
#
# vowelList = vowelFinder(sentence_string, vowels)
# print vowelList
#
# would print:
# ['a', 'e', 'i', 'o', 'y']

def vowelfinder(sentence_string, vowels):
    i=0
    vowelsinsen=[]
    acount=    0
    ecount=   0
    icount=  0
    ocount= 0
    ucount=0
    ycount=0
    #TESTS
    # print vowels
    # print sentence_string
    # print i
    for x in range(0, len(sentence_string)):
        if sentence_list[i] in vowels:
               if sentence_list[i]=="a":
                   acount=acount+1
               elif sentence_list[i]=="e":
                   ecount=ecount+1
               elif sentence_list[i]=="i":
                   icount=icount+1
               elif sentence_list[i]=="o":
                   ocount=ocount+1
               elif sentence_list[i]=="u":
                   ucount=ucount+1
               elif sentence_list[i]=="y":
                   ycount=ycount+1
               if sentence_list[i] in vowelsinsen:
                    i=i+1
               else:
                    vowelsinsen.append(sentence_list[i])
                    i=i+1


    print "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print "All of the vowels in,",sentence_string,", are",vowelsinsen
    print "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print "There were", acount," a's,",ecount,"e's,",icount,"i's,", ocount,"o's,",ucount,"u's, and ", ycount,"y's."
vowellist= vowelfinder(sentence_string,vowels)









