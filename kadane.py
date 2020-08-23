import sys
def continuos_sub_array(nums):
    max_ending_here = 0
    max_so_far = -(sys.maxsize +1)
    for index in xrange(0,len(nums)):
        max_ending_here = max_ending_here + nums[index]
        if max_ending_here < nums[index]:
            max_ending_here = nums[index]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


if __name__ == '__main__':
    arr =[-1,-2,-3,4,-1,1,5,-6]
    print(continuos_sub_array(arr))