class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.forw = []
        self.bac = []
        self.bac.append(self.homepage)

    def visit(self, url: str) -> None:
        self.forw = []
        self.bac.append(url)

    def back(self, steps: int) -> str:
        while len(self.bac) > 1 and steps > 0:
            self.forw.append(self.bac.pop())
            steps -= 1
        
        return self.bac[-1]

    def forward(self, steps: int) -> str:
        while self.forw and steps > 0:
            self.bac.append(self.forw.pop())
            steps -= 1

        return self.bac[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)