class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        A = arr
        start, ans = None, 0
        i, L = 0, len(A)
        while i < L-1:
            if A[i] < A[i+1]:
                start = i
                while i+1 < L and A[i] < A[i+1]:
                    i += 1
            elif  A[i] == A[i+1]:
                i += 1
                start = None
            else:
                # print(i, start)
                i += 1
                if start != None:
                    ans = max(ans, i-start+1)           
        return ans
