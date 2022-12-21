class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ## 1 : The easiest method
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # nums.sort()
        # return nums
        
        ## 2 : double pointer
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans

nums = [-4,-1,0,3,10]

print(Solution().sortedSquares(nums))
