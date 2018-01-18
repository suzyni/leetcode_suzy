
def recursive_permute(nums, index, result):
    if index == len(nums):
        print "append %r" % nums
        result.append(nums)
        print "result now is %r" % result
        return

    for i in xrange(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        print "recursive from %d in nums = %r" % (i, nums)
        recursive_permute(nums, index+1, result)
        nums[index], nums[i] = nums[i], nums[index]

nums = [1,2,3]
result = []
recursive_permute(nums, 0, result)
print "result = %r" % result 
