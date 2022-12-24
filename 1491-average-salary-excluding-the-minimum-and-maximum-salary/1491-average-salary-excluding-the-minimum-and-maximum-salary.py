class Solution:
    def average(self, salary: List[int]) -> float:   
        """
        :type salary: List[int]
        :rtype: float
        """
        size = len(salary)
        salary.sort()
        print (float(sum(salary[1:size-1])))
        return sum(salary[1:size-1])/(size-2)
    