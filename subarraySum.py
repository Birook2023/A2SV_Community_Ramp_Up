class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixsum = c = 0
        d = dict()
        
        d[0]=1
        
        for i in nums:
            prefixsum += i
            if prefixsum - k in d:
                c += d[prefixsum - k]
            if prefixsum in d:
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return c   
