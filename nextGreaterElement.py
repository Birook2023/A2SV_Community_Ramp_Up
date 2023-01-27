class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        outcome = []
        
        for i in nums1:
            found = 0
            for j in range((nums2.index(i)+1), len(nums2)):
                if nums2[j] > i:
                    outcome.append(nums2[j])
                    found = 1
                    break
            if found == 0:
                outcome.append(-1)
        return outcome
                       
