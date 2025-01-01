from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}

        def helper(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            
            if all(n == 0 for n in needs):
                return 0

            res = sum(p * n for p, n in zip(price, needs))
            
            for s in special:
                if all(s[i] <= needs[i] for i in range(len(needs))):
                    remain = [needs[i] - s[i] for i in range(len(needs))]
                    res = min(res, s[-1] + helper(remain))
            
            memo[tuple(needs)] = res
            return res

        return helper(needs)
