class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ps = defaultdict(int)
        
        count = 0
        sum = 0
        for num in nums:
            sum += num % 2
            if sum - k == 0:
                count += 1
            count += ps[sum - k]
            ps[sum] += 1

        return count
