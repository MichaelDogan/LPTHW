from sys import argv

script , filename = argv

print "We're going to read and print %r." % filename
print "Hit RETURN to continue"

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print "Now I'm going to read the file."

content = target.read()

print "Here is your file:"

print "%s" % content

print "And finally, we close it."
target.close()