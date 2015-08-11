# Dice Rolling Simulator :
# http://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# The Goal: Like the title suggests, this project involves writing a program 
# that simulates rolling dice.  When the program runs, it will randomly choose
# a number between 1 and 6. (Or whatever other integer you prefer - the number
# of sides on the die is up to you.) The program will print what that number
# is.  It should then ask you if you'd like to roll again.  For this project,
# you'll need to set the min and max number that your dice can produce.  For
# the average die, that means a minimum of 1 and a maximum of 6.  You'll also
# want a function that randomly grabs a number within that range and prints it
#
# Concepts to keep in mind:
#	Random
#	Integer
#	Print
#	While Loops
#	

# get useful modules
from random import randrange

# define the die
sides_on_die = 6 

def roll(sides):
	return randrange(1,sides + 1) # randrange(startOfRangeInclussive, EndOfRangeNonInclusive)
	
# print roll(sides_on_die)

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
exceptions = 0

for x in range(0,1000000): # 1 million roles!
	my_number = roll(sides_on_die)
	if my_number == 6:
		count6 += 1
	elif my_number == 5:
		count5 += 1
	elif my_number == 4:
		count4 += 1
	elif my_number == 3:
		count3 += 1
	elif my_number == 2:
		count2 += 1
	elif my_number == 1:
		count1 += 1
	else:
		exceptions += 1
print "1 occurred %d times" % count1
print "2 occurred %d times" % count2
print "3 occurred %d times" % count3
print "4 occurred %d times" % count4
print "5 occurred %d times" % count5
print "6 occurred %d times" % count6
print "Out of Range occurred %d times" % exceptions

raw_input("Roll again?")