haystack = "mississippi"
needle = "issip"

h = len(haystack)
n = len(needle)
head = 0
tail = 0
cur = 0

while head < h-n+1:
    if needle[cur] == haystack[tail]:
	cur += 1
	tail += 1
        print "match. cur = %d, head = %d, tail = %d" % (cur, head, tail)
	if cur == n:
	    print "sccess!! head = %d" % head
    else:
        print "no match. head +1"
	head += 1
	while head <= tail:
	    if haystack[head] != needle[0]:
		head += 1
            else:
                break
        print "head forward to %d, haystack[head] = %r" % (head, haystack[head])
	tail = head
	cur = 0
print "failed!!"

