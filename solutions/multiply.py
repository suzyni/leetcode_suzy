num1 = "123"
num2 = "45"
m = len(num1)
n = len(num2)
mul = [0 for x in xrange(m+n)]

for i in xrange(m-1, -1, -1):
    for j in xrange(n-1, -1, -1):
	p1, p2 = i+j, i+j+1
	ad = int(num1[i]) * int(num2[j]) + mul[p2]
	mul[p1] += ad / 10
	mul[p2] = ad % 10
        print "mul now is %r" % mul

if mul[0] == 0:
    mul.pop(0)
result = "".join(map(str, mul))

print "result is %r" % result
