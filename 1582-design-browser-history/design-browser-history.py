class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]  # List to store browsing history
        self.current = 0           # Index of current page
        self.size = 1              # Current size of valid history (for forward clearing)

    def visit(self, url: str) -> None:
        # When visiting a new URL, clear all forward history
        self.current += 1
        if self.current < len(self.history):
            self.history[self.current] = url
        else:
            self.history.append(url)
        self.size = self.current + 1  # Update size to current position + 1

    def back(self, steps: int) -> str:
        # Move back by steps, but not beyond the beginning
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward by steps, but not beyond the valid history
        self.current = min(self.size - 1, self.current + steps)
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)