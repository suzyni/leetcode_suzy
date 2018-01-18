from sys import argv

script, s = argv

result = s[0]
l = 1
        
        # index[i][j] = 1 if s[i:j] is palindromic, 0 if not
index = [[0 for col in range(1000)] for row in range(1000)]
        
for i in range(len(s)):
    index[i][i] = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        index[i][i+1] = 1
        result = s[i]+s[i+1]

for length in range(3, len(s)+1):
    print "length: %d" % length

    for i in range(len(s)-length+1):
        if index[i+1][i+length-2] == 1 and s[i] == s[i+length-1]:
            index[i][i+length-1] = 1
            print "match(%d-%d): %s" % (i, i+length-1, s[i:i+length])
            if length > l:
                result = s[i:i+length]
        else:
            index[i][i+length] = 0
            
print "result: %r" % result
