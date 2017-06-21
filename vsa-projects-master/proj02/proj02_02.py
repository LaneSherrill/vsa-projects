# Name:Lane Sherrill
# Date:June 20, 2017

# proj02_02: Fibonaci Sequence

print """
    Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
    sequence is a sequence of numbers where the next number in the sequence is the sum of the 
    previous two numbers in the sequence. The sequence looks like this: 
    1, 1, 2, 3, 5, 8, 13...
"""
print " "

aon= raw_input("How many Fibonacci numbers do you want?: ")

numc = 1
nump = 0
sum = numc + nump
print sum
for x in range(int(aon)-1):
    sum = int(nump)+int(numc)
    nump=numc
    numc=sum
    print sum

numc=1
nump=0
sum= int(numc)+ int(nump)

aon= raw_input("How many powers of two do you want?: ")

for x in range(int(aon)+1):
    sum= int(nump)+ int(numc)
    numc=sum
    nump=numc
    if sum!= 1:
        print sum





