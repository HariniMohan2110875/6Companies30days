#User function Template for python3

class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        bracket = [[0] * n for _ in range(n)]

        # Fill the DP and bracket tables
        for l in range(2, n):  # l is chain length
            for i in range(1, n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if q < dp[i][j]:
                        dp[i][j] = q
                        bracket[i][j] = k

        # Generate the string using the bracket table
        return self._construct_string(bracket, 1, n - 1)

    def _construct_string(self, bracket, i, j):
        if i == j:
            return chr(ord('A') + i - 1)
        return f"({self._construct_string(bracket, i, bracket[i][j])}{self._construct_string(bracket, bracket[i][j] + 1, j)})"

