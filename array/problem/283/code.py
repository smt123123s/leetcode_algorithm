class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # double pointer => update != 0 first => the remain are 0
        slow = 0
        fast = 0
        size = len(nums)
        while fast < size :
            if(nums[fast]) != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < size:
            nums[slow] = 0
            slow += 1
        return nums
        
nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))