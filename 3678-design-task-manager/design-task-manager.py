class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}  # taskId -> (userId, priority)
        self.heap = []   # (-priority, -taskId)
        
        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.tasks:
            userId, old_priority = self.tasks[taskId]
            self.tasks[taskId] = (userId, newPriority)
            # Push the updated priority to heap
            heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.tasks:
            del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_priority, neg_taskId = heapq.heappop(self.heap)
            taskId = -neg_taskId
            expected_priority = -neg_priority
            
            # Check if task exists and has the expected priority
            if (taskId in self.tasks and 
                self.tasks[taskId][1] == expected_priority):
                userId = self.tasks[taskId][0]
                del self.tasks[taskId]
                return userId
        
        return -1
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()