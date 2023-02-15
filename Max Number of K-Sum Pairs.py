class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        cnt = 0
        
        while l < r:
            twoSum = nums[l] + nums[r] - k
            
            if twoSum < 0:
                l += 1
                
            elif twoSum > 0:
                r -= 1
                
            else:
                cnt += 1
                l += 1
                r -= 1
        
        return cnt
