class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        temp = len(nums) + 1
        ans = temp
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                ans = min(ans, j-i+1)
                target += nums[i]
                i += 1
        return ans % temp
