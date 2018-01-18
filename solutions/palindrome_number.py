import math
from sys import argv
from sys import exit

script, x = argv

l = int(math.floor(math.log10(float(x)))) # how many digits are in x? l+1i
print "x is of 10^%d long." % l

for it in range(int(l/2)):
    print "the %dth iteration:" % it
            # left digit No. it:
            #     the right digit of the left (l-it) digits
    i = (x // (10**(l-it))) % 10
    print "i = %d  " % i,            
            # right digit No. it:
            #     the left digit of the right (it) digits
    j = (x % 10) // (10**it)
    print "j = %d" % j
    if i == j:
        print "i = j. going on..."
        continue
    else:
        print "result is False."
        exit(0)
        
print "result is true!"
