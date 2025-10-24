class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        result = 0
        l = 0
        for r in range(len(s)):
            if s[r] in visited and visited[s[r]] >= l:
                l = visited[s[r]] + 1
            visited[s[r]] = r
            result = max(result, r-l+1)

        return result