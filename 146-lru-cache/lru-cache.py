class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(int)
        self.used = defaultdict(int)
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.count += 1
            self.used[key] = self.count
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity or key in self.cache:
            self.cache[key] = value
            self.used[key] = self.count
        else:
            lru = key
            n = float('inf')
            for k, v in self.used.items():
                if self.used[k] < n:
                    lru = k
                    n = v

            del self.used[lru]
            del self.cache[lru]         
            self.cache[key] = value
            self.used[key] = self.count

        self.count += 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)