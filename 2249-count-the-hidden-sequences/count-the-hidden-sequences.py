class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        prifix = [0] * (n+1)
        for i in range(n):
            prifix[i+1] = prifix[i] + differences[i]

        min_prefix = min(prifix)
        max_prefix = max(prifix)

        min_range = lower - min_prefix
        max_range = upper - max_prefix

        actual_lower = max(lower, min_range)
        actual_upper = min(upper, max_range)

        return 0 if actual_upper < actual_lower else actual_upper - actual_lower + 1