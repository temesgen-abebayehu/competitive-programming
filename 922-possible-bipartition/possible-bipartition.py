class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        color = [0] * (n+1)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)


        for i in range(1, n+1):
            if color[i] == 0:
                queue = deque([i])
                color[i] = 1

                while queue:
                    p = queue.popleft()
                    
                    for n in graph[p]:
                        if color[n] == 0:
                            color[n] = -color[p]
                            queue.append(n)
                        elif color[n] == color[p]:
                            return False

                        

        return True
        