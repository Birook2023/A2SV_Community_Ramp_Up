class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        result = 0
        totLen = firstLen + secondLen
        
        for _ in range(2 - (firstLen == secondLen)):
            it = iter(nums)
            maxSeenSum = firstSum = sum(next(it) for _ in range(firstLen))
            secondSum = sum(next(it) for _ in range(secondLen))
            result = max(result, maxSeenSum + secondSum)
            
            for index in range(firstLen + secondLen, n):     
                firstSum += nums[index - secondLen] - nums[index - totLen]   
                secondSum += nums[index] - nums[index - secondLen]   
                maxSeenSum = max(firstSum, maxSeenSum) 
                result = max(result, maxSeenSum + secondSum)
            
            firstLen, secondLen = secondLen, firstLen
        
        return result
