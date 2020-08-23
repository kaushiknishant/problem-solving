def find_subsets(nums):
    n = len(nums)
    for i in xrange(0,(1<<n)):
        print "{"
        for j in xrange(0,n):
            if (i & (1<<j)) > 0:
                print nums[j]
        print "}"

if __name__ == "__main__":
    arr =[1,2,3]
    find_subsets(arr)