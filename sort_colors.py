# dutch flag algo
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1
        while mid<=high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,1,0,1,1,2,1,2,0,0,0,1]
    res = sol.sortColors(nums)
    print(res)