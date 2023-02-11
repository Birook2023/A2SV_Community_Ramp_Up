class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #  [1 , 7 , 3 , 6 , 5 , 6]
        #  i     0   1    2    3   
        # left   0   1    8    11 
        # right  27  19   17   11 = True, return i

        for i in range(len(nums)): 
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i  
        return -1
