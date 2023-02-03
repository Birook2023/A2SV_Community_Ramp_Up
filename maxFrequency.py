class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        inc = 0
        nums.sort()

        for index in range(len(nums)):
            k += nums[index]

            if k < nums[index] * (index - inc + 1):
                k -= nums[inc]
                inc += 1

        return index - inc + 1
