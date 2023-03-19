class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in range(len(nums)-1):
            # this will figure out the max loot can be collected at each point of the time
            temp = max(nums[n] + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        rob3,rob4 = 0,0
        for n in range(1,len(nums)):
            # this will figure out the max loot can be collected at each point of the time
            temp = max(nums[n] + rob3, rob4)
            rob3 = rob4
            rob4 = temp

        return max(rob2,rob4)