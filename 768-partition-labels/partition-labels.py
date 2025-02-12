class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occu = {char: ind for ind, char in enumerate(s)}
        parts = []
        start = 0
        end = 0
        
        for i in range(len(s)):
            end = max(end, last_occu[s[i]])

            if i == end:
                parts.append(end - start + 1)
                start = i + 1

        return parts
            