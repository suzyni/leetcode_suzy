#from sys import argv

#script, nums1, nums2 = argv

nums1 = [1,2]
nums2 = [3,4]

m = len(nums1)
n = len(nums2)

print "m = %d, n = %d" % (m, n)

p1 = 0
p2 = 0
pick = 0

for i in range(0, (m+n)/2):
    if p1 == m and p2 < n:
        pick = nums2[p2]
        print "pick nums2[%d] = %r" % (p2, pick)
        p2 += 1
    elif p1 < m and p2 == n:
        pick = nums1[p1]
        print "pick nums1[%d] = %r" % (p1, pick)
        p1 += 1
    else:
        if nums1[p1] <= nums2[p2]:
            pick = nums1[p1]
            print "pick nums1[%d] = %r" % (p1, pick)
            p1 += 1
        else:
            pick = nums2[p2]
            print "pick nums2[%d] = %r" % (p2, pick)
            p2 += 1

if p1 == m and p2 < n:
    if (m+n) % 2 == 0:
        pick = float(pick+nums2[p2])/2
    else:
        pick = nums2[p2]
elif p1 < m and p2 == n:
    if (m+n) % 2 == 0:
        pick = float(pick+nums1[p1])/2
    else:
        pick = nums1[p1]
else:
    if nums1[p1] <= nums2[p2]:
        if (m+n) % 2 == 0:
            pick = float(pick+nums1[p1])/2
        else:
            pick = nums1[p1]
    else:
        if (m+n) % 2 == 0:
            pick = float(pick+nums2[p2])/2
        else:
            pick = nums2[p2]

print "median: %r" % pick
