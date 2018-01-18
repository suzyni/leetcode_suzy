nums = [2,3,1]
n = len(nums)
found = 0
if n > 1:
    for i in xrange(n-2, -2, -1):
        print "i = %d" % i
	if i>=0 and nums[i+1]>nums[i]:
            print "found switch point i = %d" % i
	    for j in xrange(n-1, i, -1):
		if nums[j] > nums[i]:
                    print "switch nums[%d] with nums[%d]" % (i, j)
		    nums[i], nums[j] = nums[j], nums[i]
		    nums[i+1:] = sorted(nums[i+1:])
		    found = 1
		    break
	    if found == 1:
                print "result = %r" % nums
		break
    else:
        nums.reverse()
        print "this is the largest list. result = %r" % nums
