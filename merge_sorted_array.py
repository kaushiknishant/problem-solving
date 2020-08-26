def merge(nums1,m,nums2,n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in xrange(m,n):
        nums1.append(0)
    l = []
    i=0
    j=0
    while i<m and j<n:
        if nums1[i] < nums2[j]:
            l.append(nums1[i])
            i += 1
        else:
            l.append(nums2[j])
            j += 1
    while i<m:
        l.append(nums1[i])
        i +=1
    while j<n:
        l.append(nums2[j])
        j +=1
    for i in xrange(m+n):
        nums1[i] = l[i]
    return nums1

if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,5,6]
    print(merge(nums1,3,nums2,3))