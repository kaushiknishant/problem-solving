def counting_sort(nums):
    output = [0]*len(nums)
    freq = [0]*(max(nums) + 1)
    for num in nums:
        freq[num] += 1
    for index in xrange(1,len(freq)):
        freq[index] += freq[index-1]
    for index in xrange(len(nums)):
        output[freq[nums[index]]-1] = nums[index]
        freq[nums[index]] -= 1
    for index in xrange(len(nums)):
        nums[index] = output[index]
    return nums

if __name__ == '__main__':
    nums=[2,2,3,3,4,4,4,2,0]
    print(counting_sort(nums))