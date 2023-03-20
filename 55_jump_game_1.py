class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        #  optimal solution
        N = len(nums)
        dp = [0] * N

        last_true = 0

        for i in reversed(range(N)):
            if i == N-1:
                dp[i] = 1
                last_true = i
            else:
                if i + nums[i] >= last_true:
                    dp[i] = 1
                    last_true = i

        print(last_true)
        print(dp)
        return dp[0] == 1