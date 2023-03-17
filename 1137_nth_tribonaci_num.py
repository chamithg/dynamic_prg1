class Solution:
    def tribonacci(self, n: int) -> int:
        if n ==0: return 0
        if n ==1: return 1
        if n ==2: return 1

        prev1,prev2,cur = 0,1,1
        position = 2

        while position < n:
            prev1,prev2,cur = prev2,cur,cur+prev2+prev1
            position +=1
            

        return cur