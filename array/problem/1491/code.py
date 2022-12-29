class Solution:
    def average(self, salary: list[int]) -> float:
        maxValue = max(salary)
        minValue = min(salary)
        total = sum(salary) - maxValue - minValue
        return total / (len(salary) - 2)


salary = [4000,3000,1000,2000]
print(Solution().average(salary))