class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
        answer = list(map(lambda x:x[0],questions))
        size = len(questions)
        
        for i in range(size-2,-1,-1):
            brainPower = questions[i][1]
            current = answer[i]
            if brainPower < (size-1) - i:
                current += answer[i+brainPower+1]

            answer[i] = max(current,answer[i+1])
        print(answer)
        return answer[0]