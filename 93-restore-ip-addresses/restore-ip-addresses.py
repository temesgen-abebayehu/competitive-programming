class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append('.'.join(parts))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start: end]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(end, parts + [segment])

        backtrack(0, [])
        return res