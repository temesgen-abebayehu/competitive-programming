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
        emp_dic = {}
        for emp in employees:
            emp_dic[emp.id] = emp

        def dfs(id):
            total = emp_dic[id].importance
            for id in emp_dic[id].subordinates:
                total += dfs(id)

            return total
            
        return dfs(id)
