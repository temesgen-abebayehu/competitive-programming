class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arrive = [(enq, pro, idx) for idx, (enq, pro) in enumerate(tasks)]
        arrive.sort()

        time = 0
        i = 0
        ans = []
        order = []
        n = len(tasks)
        
        while i<n or order:
            if not order and arrive[i][0] > time:
                time = arrive[i][0]

            while i < n and arrive[i][0] <= time:
                enq, pro, idx = arrive[i]
                heapq.heappush(order, (pro, idx, enq))             
                i += 1

            if order:
                task = heapq.heappop(order)
                ans.append(task[1])
                time += task[0]

        return ans