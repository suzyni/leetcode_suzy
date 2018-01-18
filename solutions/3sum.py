nums = [-1,0,1,2,-1,-4]
n = len(nums)
result = []
dict = {}
        
for i in range(0, n):
    for j in range(i+1, n):
        x = 0-nums[i]-nums[j]
        if x in dict:
            dict[x].append([i, j])
        else:
            dict[x] = [[i, j]]
print dict
for k in range(0, n):
    if nums[k] in dict:
        for [i, j] in dict[nums[k]]:
            if k != i and k != j:
                result.append(sorted([nums[i], nums[j], nums[k]]))
                print "i=%d, j=%d, k=%d. result appended: %r" % (i, j, k, result)
