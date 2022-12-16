## double pointer
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        size = len(nums)
        while fast < size :
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
        

#test sample
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
# expected ans => 4
