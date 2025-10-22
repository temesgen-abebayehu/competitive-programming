class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lake = {}
        dry_day = []
        result  = [-1] * len(rains)
        for day, lake in enumerate(rains):
            if lake == 0:
                dry_day.append(day)
                result[day] = 1
            else:
                if lake in full_lake:
                    d = bisect_right(dry_day, full_lake[lake])
                    if d<len(dry_day) and dry_day[d] < day:
                        result[dry_day[d]] = lake
                        dry_day.pop(d)
                    else:
                        return []
                full_lake[lake] = day


        return result
            