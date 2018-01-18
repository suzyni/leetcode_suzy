from sys import exit

s = "bbcbbcbcbbcaabcacb"
p = "a*.*ac*a*a*.a..*.*"

def matching(s, p, si, pi, stopsi, stoppi):
    result, si, pi = forward(s, p, si, pi)
    print "forward to si = %d, pi = %d, result = %d" % (si, pi, result)
    if result == 0:
        return False, si, pi
    elif result == 1:
        return True, si, pi
    else: # result == 2
        while True:
            b, si, pi = backward(s, p, si-1, pi, stopsi, stoppi) # reserve si, pi as backtrack points
            print "backtrack to si = %d, pi = %d, result = %d" % (si, pi, b)
	    if b == 0:
                return False, si, pi
	    else:
                if si == 0 and pi < len(p):
                    temppi = pi
                    while temppi > 0:
                        temppi -= 1
                        if p[temppi] == '*':
                            temppi -= 1
                        else:
                            pi = temppi
                            print "escape to the single %r!!!!!!!!!!!!!!" % p[pi]
                            break
	        f, x, y = matching(s, p, si, pi+2, si, pi+2) # forward based on current backtrack points
                print "forward (%d, %d) to x = %d, y = %d, result = %d" % (si, pi+2, x, y, f)
	        if f == 1:
		    return True, si, pi
	        else: # f == 0 or 2, check for matching prefix
                    continue
 
def forward(s, p, si, pi):
    while pi < len(p) and si < len(s):
        if peek(p, pi) == '*':
            if match(s[si], p[pi]):
                print "%s matches %s, si +1" % (s[si], p[pi])
                si += 1
            else:
                print "%s doesn't match %s, pi +2" % (s[si], p[pi])
                pi += 2
        else:
            if match(s[si], p[pi]):
                print "%s matches %s, si +1, pi +1" % (s[si], p[pi])
                si += 1
                pi += 1
            else:
                break # no match
                
    if pi == len(p) and si == len(s):
        return 1, si, pi # match
    elif pi == len(p)-2 and peek(p, pi) == '*' and si == len(s):
        return 1, si, pi # match
    elif pi == len(p) and si < len(s):
        return 0, si, pi # no match
    elif peek(p, pi) is not '*':
        pi -= 1
        if p[pi] == '*':
            return 2, si, pi-1
        else:
            return 2, si, pi
    elif peek(p, pi) == '*' and si == len(s):
        temp = pi
        while temp < len(p):
            if peek(p, temp) == '*':
                temp += 2
            else:
                return 2, si, pi
        return 1, si, pi
    else:
        return 2, si, pi # need backtrack to determine

def backward(s, p, si, pi, stopsi, stoppi):
    while pi >= stoppi and si >= stopsi:
        if peek(p, pi) == '*':
            if match(s[si], p[pi]):
                if si >= 0:
                    print "si backtracked to %d" % si
                    return 1, si, pi # backtracked one step
                else:
                    return 0, si, pi
            else:
                pi -= 1
                if p[pi] == '*':
                    pi -= 1
                    print "no *, pi moving back to %d" % pi
        else:
            if match(s[si], p[pi]):
                si -= 1
                pi -= 1
                if p[pi] == '*':
                    pi -= 1
                print "no *, moving back to %d, %d", (si, pi)
            else:
                return 0, si, pi
    return 0, si, pi # cannot find backtrack points

def peek(p, pi):
    if pi < len(p)-1:
        return p[pi+1]
    else:
        return False

def match(s, p):
    if p == '.':
        return True
    else:
        if s == p:
            return True
        else:
            return False

si = 0
pi = 0
result, si, pi = matching(s, p, si, pi, 0, 0)
print "result is %r!" % result      
