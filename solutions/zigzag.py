s = 'PAYPALISHIRING'
numRows = 3

row = numRows - 1
col = (len(s)//(numRows*2-2)+1) * (numRows-1)
table = [['' for x in range(col+1)] for y in range(row+1)]
print "row = %d, col = %d" % (row, col)

for i in range(len(s)):
    if not s[i]:
        break
    print "i = %d:" % i
    block = i // (numRows*2-2)
    remain = i % (numRows*2-2) # 0 to 2n-3
    print "\tblock %d, remain %d" % (block, remain)
    if remain < numRows:
        table[remain][block*(numRows-1)] = s[i]
        print "\t\tset table[%d][%d] = s[%d]" % (remain, block*(numRows-1), i)
    else:
        table[(numRows*2-2)-remain][block*(numRows-1)+(remain-numRows+1)] = s[i]
        print "\t\tset table[%d][%d] = s[%d]" % ((numRows*2-2)-remain, block*(numRows-1)+(remain-numRows+1), i)
        
result = ''
for r in range(row+1):
    for c in range(col+1):
        if table[r][c]:
            result += table[r][c]
     
print "result = %s" % result
