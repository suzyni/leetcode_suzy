from sys import exit

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

if not s or not words:
    print "result is []"

n = len(words[0])
result = []
head = 0
cp = 0
mark = -1

while head < len(s)-n*len(words)+1:
    print "head = %d" % head
    needles, cp = list(words), head
    while cp < len(s)-n+1:
        print "**cp = %d" % cp
        needle = s[cp:cp+n]
        if needle in needles:
            print "match %r in position %d" % (needle, cp)
	    if mark == -1:
    	        mark = cp
                print "	mark %d" % cp
  	    needles.remove(needle)
            print "needles now is %r" % needles
	    if not needles:
	        result.append(mark)
                print "needles is empty, append result: %d" % result[-1]
	        break
	    cp += n
	else:
            break
    head += 1
    mark = -1
print "result is %r" % result
exit(0)
