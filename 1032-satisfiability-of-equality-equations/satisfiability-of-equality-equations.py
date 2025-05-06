class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]

        def get(x, y):
            return find(x) == find(y)

        n = len(equations)
        root = defaultdict(str)
        size = defaultdict(int)
        
        for equ in equations:
            root[equ[0]] = equ[0]
            root[equ[-1]] = equ[-1]
            size[equ[0]] = 1
            size[equ[-1]] = 1
        
        for equ in equations:
            if equ[1] == '=':
                union(equ[0], equ[-1])

        for equ in equations:
            if equ[1] == '!':
                if get(equ[0], equ[-1]):
                    return False
                
        return True