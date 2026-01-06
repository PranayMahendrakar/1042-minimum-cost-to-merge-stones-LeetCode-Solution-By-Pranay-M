class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # Prefix sum for range sum calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        
        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]
        
        # dp[i][j] = minimum cost to merge stones[i:j+1] into as few piles as possible
        dp = [[0] * n for _ in range(n)]
        
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += range_sum(i, j)
        
        return dp[0][n - 1]