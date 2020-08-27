def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for num in nums:
        if num != val:
            nums[count] = num
            count += 1
    return count 

if __name__ == '__main__':
    nums =[0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement(nums,val))