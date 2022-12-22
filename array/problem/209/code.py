class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float("inf")


nums = [2,3,1,2,4,3]
target = 7
print(Solution().minSubArrayLen(target, nums))