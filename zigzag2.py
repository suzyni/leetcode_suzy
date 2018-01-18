s = "PAYPALISHIRING"
numRows = 3

factor = numRows*2 - 2 # every block has 2n-2 characters
block = len(s)//factor + 1
result = ''
        
        # the 0th line
print "the first line:"
for b in range(block+1):
    if factor*b < len(s):
        result += s[factor*b]
        print "s[%d] = %s" % (factor*b, s[factor*b])
    else:
        break
        
        # the 1~(n-2)th line
for i in range(1, numRows-1):
    print "the %dth line:"
    for b in range(block+1):
        if factor*b+i < len(s):
            result += s[factor*b+i]
            print "s[%d] = %s" % (factor*b+i, s[factor*b+i])
        else:
            break
        if factor*b+factor-i < len(s):
            result += s[factor*b+factor-i]
            print "s[%d] = %s" % (factor*b+factor-i, s[factor*b+factor-i])
        else:
            break
        
        # the (n-1)th line
print "the last line:"
for b in range(block+1):
    if factor*b+numRows-1 < len(s):
        result += s[factor*b+numRows-1]
        print "s[%d] = %s" % (factor*b+numRows-1, s[factor*b+numRows-1])
    else:
        break

print "result = %s" % result
