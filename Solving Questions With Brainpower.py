class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        D = [0] * len(questions) + [0] 
        for i in range(len(questions)-1,-1,-1):
            D[i] = max(questions[i][0]+ D[ min((i + 1) + questions[i][1],len(D)-1)],D[i+1])
        return D[0]
