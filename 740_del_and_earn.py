class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        map = {}
        earn = 0
        for i in nums:
            if i not in map:
                map[i] =i
            else:
                map[i] +=i
        
        sort_map = dict(sorted(map.items()))
        
        keys = []
        vals = []
        dp = [0]
        for k,v in sort_map.items():
            keys.append(k)
            vals.append(v)
            dp.append(0)
        print(keys,vals,dp)
        for i in range(len(keys)):
            if i!=0 and keys[i]-1 in keys:
                dp [i+1] = max(dp[i-1]+ vals[i],dp[i])
            else:
                dp [i+1] = dp [i] + vals[i]

        return dp[-1]