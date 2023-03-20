class Solution:
    
    #  working but slow
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [0] * N

        for i in reversed(range(N)):
            if i == N-1:
                dp[i] = 1
            else:
                for j in range(i,min(N,i+nums[i]+1)):
                    if dp[j] == 1:
                        dp[i] =1
        
        print(dp)
        return dp[0] == 1