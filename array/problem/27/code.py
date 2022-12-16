## double pointer
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        fast = 0
        size = len(nums) 
        while fast < size :
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

#test sample
nums = [0,1,2,2,3,0,4,2]
val = 2
# expected ans => 4
print(Solution().removeElement(nums, val))