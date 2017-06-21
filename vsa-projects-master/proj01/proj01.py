# Name:Lane Sherrill
# Date:June 6, 2017

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


name= raw_input("Enter your name: ")

age= raw_input("Enter your age (a postive number, i.e. 3): ")

ab= raw_input("Enter the what age you want: ")

bday= raw_input("Have you already had your birthday this year?(y or n): ")

if bday== "y":
    y= 2017+ int(ab)-int(age)
else:
    y= 2016+ int(ab)- int(age)
q= name+" will be "+ str(ab)+" in the year "

w=str(y)

if age == ab :
    print "You are " + str(ab)
elif int(age) >int(ab):
    print "You've already turned " + str(ab)+", did you forget?"
else:
    print q + w

if int(age) >0<5:
    print "You can watch G rated movies"
if 5 < int(age):
    print "You can watch PG movies"
if 12 < int(age) <17:
    print "You can watch PG13 movies"
if 17<int(age):
    print "You can watch R rated movies"

if int(age)> 150:
    print 'Stop trying the break the code'
else:
    question1= raw_input('Do you want to play again?: ')

if question1 == "yes":
    print "Too bad...I dont know how to code a loop."
else:
    print 'Oh well...I didnt know how to code a loop anyways.'

