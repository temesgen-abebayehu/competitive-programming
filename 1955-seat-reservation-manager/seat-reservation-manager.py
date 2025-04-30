class SeatManager:

    def __init__(self, n: int):
        self.free = []
        self.set = 1

    def reserve(self) -> int:
        if self.free:
            return heapq.heappop(self.free)
        else:
            ans = self.set
            self.set += 1
            return ans

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.free, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)