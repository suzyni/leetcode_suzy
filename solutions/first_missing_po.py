nums = [3, 4, -1, 1]
n = len(nums)
for i in xrange(n):
    while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
	temp = nums[i]
        nums[i] = nums[temp-1]
        nums[temp-1] = temp
        print "mid-result: %r" % nums
for i in xrange(n):
    if nums[i] != i+1:
	print "result is %r" % i+1
print "result is %r" % n+1
