class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        for i in range(len(nums)):
            nums[i] = int(nums[i])

        nums.sort()

        nums.reverse()

        kth = nums[k-1]
        
        return str(kth)
        
