from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#user_input = raw_input('Now enter something... go ahead... ANYTHING will do! : ')  
user_input = raw_input("Are you sure %s is the third variable you want to use?" % third)

print "You said %s " % user_input

#  Tried to do something like:
#   user_input = raw_input('Is %s ok for your third variable?') % third
#   but that doesn't work.  It prints the %s literally and crashes on the % third  
#   why?  Perhaps I'll learn in a later lesson
#  Figured it out!  as above in line 11... it ALL has to be in the () called by raw_input
#  See ex16.py for more!