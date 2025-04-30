class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.large = []
        for num in nums:
            if len(self.large) < k:
                heapq.heappush(self.large, num)
            else:
                heapq.heappushpop(self.large, num)

    def add(self, val: int) -> int:    
        if len(self.large) < self.k:
            heapq.heappush(self.large, val)
        else:
            heapq.heappushpop(self.large, val)

        return self.large[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)