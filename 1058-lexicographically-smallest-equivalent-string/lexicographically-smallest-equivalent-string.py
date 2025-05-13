class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x

        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
        
        root = [i for i in range(26)]
        for u, v in zip(s1,s2):
            a = ord(u) - ord('a')
            b = ord(v) - ord('a')
            union(a,b)

        res = []
        for c in baseStr:
            x = ord(c) - ord('a')
            parent = find(x)
            res.append(chr(parent + ord('a')))
        
        return ''.join(res)