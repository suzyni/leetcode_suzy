nums = [4,5,6,7,1,2,3]
target = 7

if not nums:
    pass
n = len(nums)

if nums[0] > target:
    i = n-1
    while i >= 0:
        print "searching... i = %d" % i
	if target == nums[i]:
	    print "found! result = %d" % i
	i -= 1
	if i > 0 and nums[i] < nums[i-1]:
	    break
else:
    i = 0
    while i <= n-1:
        print "searching... i = %d" % i
	if target == nums[i]:
	    print "found! result = %d" % i
	i += 1
	if i < n-1 and nums[i] > nums[i+1]:
	    break

