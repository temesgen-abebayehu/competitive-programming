class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = defaultdict(set)
        indegre = defaultdict(int)
        for a, b in richer:
            graph[a].add(b)
            indegre[b] += 1

        que = deque()
        for i in range(n):
            if indegre[i] == 0:
                que.append(i)

        ans = [i for i in range(n)]

        while que:
            curr = que.popleft()
            for negibor in graph[curr]:
                if quiet[ans[curr]] < quiet[ans[negibor]]:
                    ans[negibor] = ans[curr]
                indegre[negibor] -= 1
                if indegre[negibor] == 0:
                    que.append(negibor)
        return ans