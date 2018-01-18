height = [1,2,3,4,5,6]
print height
n = len(height)
max = 0
i = 0
j = n-1
while i < j:
    vol = min(height[i], height[j]) * (j-i)
    if vol > max:
        max = vol
    if height[i] >= height[j]:
        j -= 1
    else:
        i += 1
print "max = %d" % max
