def onejump(nums, count):
    n = len(nums)
    if n == 1:
        return
    for i in xrange(1, nums[0]+1):
        if i > n:
            break
        else:
            print "count = %d, jump from %d to %d" % (count, nums[0], nums[i])
            onejump(nums[i:], count+1)

nums = [2, 3, 1, 1, 4]
count = 0
onejump(nums, count)
print "result = %d" % count
