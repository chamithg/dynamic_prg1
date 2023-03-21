class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        jumps = [0] * N
        # [2,3,1,1,4]
        # [0,1,2,1,0]

        for i in reversed(range(N)):
            if i == N-1:
                jumps[i] = 0
            elif i + nums[i] >= N-1:
                jumps[i] = 1
            else:
                temp = sorted(jumps[i:i+nums[i]+1])
                while 0 in temp:
                    temp.remove(0)
                if temp:
                    jumps[i] = temp[0] +1
                else:
                    jumps[i] =0
        
        return jumps[0]
