class Solution:
    def countOdds(self, low: int, high: int) -> int:
        pre = lambda x : (x+1) >> 1
        return pre(high) - pre(low - 1)

low = 3
high = 7
print(Solution().countOdds(low, high))