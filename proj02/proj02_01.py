# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))

if age>100:
    print "This won't work at all now, good job...."

bday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if bday == "Y":
    year = 2017
else:
    year = 2016

year2= year

while 100 - age + year > year2:
    print str(year2)
    year2= year2 +1

print name, "will turn 100 in the year ", year2,"."