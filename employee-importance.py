"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id] = [emp.importance,emp.subordinates]
        return self.findImportance(graph,id)
    def findImportance(self,graph,id):
        if len(graph[id][1]) == 0:
            return graph[id][0]
        total = 0

        for subordinate in graph[id][1]:
            total += self.findImportance(graph,subordinate)
        return total+graph[id][0]