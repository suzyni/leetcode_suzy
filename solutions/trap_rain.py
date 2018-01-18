height = [5,2,1,2, 1, 5]
n = len(height)
hills = []
rain = 0

for i in xrange(n):
    if i == 0 and height[1] < height[0]:
	hills.append(0)
        print "append 0"
    elif i == n-1 and height[n-2] < height[n-1]:
	hills.append(n-1)
        print "append %r" % int(n-1)
    elif height[i-1] < height[i] and height[i+1] < height[i]:
	hills.append(i)
        print "append %d" % i

print "hills = %r" % hills

if len(hills) <= 1:
    print "result is 0"

i = 1
while i < len(hills)-1
for j in xrange(len(hills)-1):
    left, right = hills[j], hills[j+1]
    h = min(height[left], height[right])
    print "rain between %d and %d, height of %d" % (height[left], height[right], h)
    for k in xrange(left+1, right):
	rain += h-height[k]
        print "\t%r added!!" % int(h-height[k])

print "%d units of rain is trapped!" % rain
