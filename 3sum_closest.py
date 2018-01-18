nums = [-1,2,1,-4]
target = 1

n = len(nums)
nums = sorted(nums)
greater = 0
less = 0
result = 0
        
for i in range(0, n-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l = i+1
    r = n-1
    while l < r:
        print "i = %d, l = %d, r = %d" % (i, l, r)
        sum = nums[i]+nums[l]+nums[r]
        print "%d + %d + %d = %d" % (nums[i], nums[l], nums[r], sum)
        if sum < target:
            less = target-sum
            if greater == 0:
                l += 1
                print "l + 1"
                while nums[l] == nums[l-1] and l < r:
                    l += 1
                    print "l + 1"
            elif less < greater and less < result:
                result = less
                print "result = less"
                break
            elif greater < less and greater < result:
                result = greater
                print "result = greater"
                break
        else:
            greater = sum-target
            if less == 0:
                r -= 1
                print "r - 1"
                while nums[r] == nums[r+1] and l < r:
                    r -= 1
                    print "r - 1"
            elif less < greater and less < result:
                result = less
                print "result = less"
                break
            elif greater < less and greater < result:
                result = greater
                print "result = greater"
                break

print "result = %d" % result
