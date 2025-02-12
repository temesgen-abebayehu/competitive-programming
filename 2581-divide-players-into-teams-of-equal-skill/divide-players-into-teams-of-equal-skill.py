class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 1
        r = len(skill) - 2
        first_group = skill[0] + skill[-1]
        result = skill[0] * skill[-1]

        while l < r:
            if skill[l] + skill[r] == first_group:
                result += skill[l] * skill[r]
            else:
                return -1
            l += 1
            r -= 1

        return result