stack = []
s = "({[]}[]){}"
for i in range(0, len(s)):
    if s[i] in ('(', '{', '['):
	stack.append(s[i])
        print "push %r in stack." % s[i]
    else:
	if len(stack) == 0:
	    print "False! nothing to match in stack"
        x = stack.pop()
	if x == '(' and s[i] == ')':
            print "pop %r. stack now: %r" % (x, stack)
	    continue
	elif x == '[' and s[i] == ']':
            print "pop %r. stack now: %r" % (x, stack)
	    continue
	elif x == '{' and s[i] == '}':
            print "pop %r. stack now: %r" % (x, stack)
	    continue
        else:
            print "False! not match in stack. %r VS %r" % (s[i], x)
if len(stack) == 0:
    print "True!"
else:
    print "False! There's something left in the stack. stack now: %r" % stack
