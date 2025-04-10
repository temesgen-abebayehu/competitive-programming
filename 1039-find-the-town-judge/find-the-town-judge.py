class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        people = defaultdict(set)
        for p, t in trust:
            people[p].add(t)

        judge = defaultdict(int)
        for p in people:
            for i in people[p]:
                judge[i] += 1

        ans = []
        for i in judge:
            if judge[i] == n-1 and i not in people:
                ans.append(i)
        if len(ans) == 1:
            return ans[0]
        else:
            return -1

        