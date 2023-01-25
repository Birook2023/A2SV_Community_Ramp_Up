class Solution:
    def sortSentence(self, s: str) -> str:
        """
        """
        s = s.split()
        dic = {}
        
        for word in s:
            num = word[-1]
            dic[int(num)] = word[:-1]
            
        ans = ""    
        for ID in range(1,len(s)+1):
            ans += dic[ID]
            ans += " "
        
        return ans[:-1]
                       
      
        
            
            
        
