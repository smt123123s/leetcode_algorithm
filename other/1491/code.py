class Solution:
    def average(self, salary: list[int]) -> float:
        maxValue = max(salary)
        minValue = min(salary)
        total = sum(salary) - maxValue - minValue
        return total / (len(salary) - 2)

# test sample
nums = [1500, 2500, 3000, 4000]
print(Solution().average(nums));