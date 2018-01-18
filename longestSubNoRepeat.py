from sys import argv

script, s = argv

i = 0
j = i + 1
l = 1
max_len = 1
      
while j < len(s):
    print "i = %d, j = %d, substring is %r" % (i, j, s[i:j+1])
    k = s[i:j].find(s[j])
    if k == -1:
        l += 1
        j += 1
        if l > max_len:
            max_len = l
            print "k = -1, so l is now %d, max_len is %d, and i=%d, j=%d" % (l, max_len, i, j)
    else:
        l -= (k-i)
        i = k + 1
        j += 1
        print "k = %d, so l is now %d, and i=%d, j=%d" % (k, l, i, j)

print "longest substring length without repeat: %d" % max_len
