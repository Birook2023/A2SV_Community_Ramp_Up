class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k:
            return '0'

        result = []
        for n in num:

            while k and result and n < result[-1]:
                result.pop()
                k -= 1
                
            result.append(n)

        if k:
            del result[-k:]

        result = ''.join(result)

        result = result.lstrip('0')
        return result if result else '0'
