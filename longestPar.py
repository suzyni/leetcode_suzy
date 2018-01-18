s = ")(())((()()()"
n = len(s)
if n < 2:
    print "n < 2."

stack = []

for i in xrange(n):
    print "i = %d, s[i] = %r:" % (i, s[i])
    if len(stack) == 0:
	stack.append(i)
        print "stack append. %r" % stack
    elif s[i] == ')' and s[stack[-1]] == '(':
	stack.pop()
        print "stack pop. %r" % stack
    else:
	stack.append(i)
        print "stack append. %r" % stack

result = 0
for i in xrange(len(stack)-1):
    delta = stack[i+1]-stack[i]-1
    print "delta = %d" % delta
    if delta < result:
	result = delta
        print "result = %d" % result

print "result = %d" % result
