nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
n = len(nums)
nums = sorted(nums)
print "sorted nums = %r" % nums
result = []
if n < 4:
    print "result = %r" % result
if n == 4:
    sum = 0
    for i in range(0, n):
	sum += nums[i]
    if sum == target:
	result.append(nums)
	print "result = %r" % result

for k in range(0, n-3):
    sum3 = target-nums[k]
    print "k = %d, nums[k] = %d, searching for 3sum of %d" % (k, nums[k], sum3)
    for i in range(k+1, n-2):
	#if nums[i] > sum3:
	#    break
	#if i > 0 and nums[i] == nums[i-1]:
	#    continue
	l = i+1
	r = n-1
	while l < r:
	    sum = nums[i]+nums[l]+nums[r]
            print "%d+%d+%d = %d" % (nums[i], nums[l], nums[r], sum)
	    if sum < sum3:
		l += 1
	    elif sum > sum3:
		r -= 1
	    else:
		if [nums[k], nums[i], nums[l], nums[r]] not in result:
		    result.append([nums[k], nums[i], nums[l], nums[r]])
                    print "appending [%d, %d, %d, %d]" % (nums[k], nums[i], nums[l], nums[r])
		#while l < r and nums[l] == nums[l+1]:
		#    l += 1
		#while l < r and nums[r] == nums[r-1]:
		#    r -= 1
		l += 1
		r -= 1

print "result = %r" % result
