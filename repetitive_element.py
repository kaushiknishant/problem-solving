# Hare & Tortoise algorithm
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hare = tortoise = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,4,2,2]
    res = sol.findDuplicate(nums)
    print(res)