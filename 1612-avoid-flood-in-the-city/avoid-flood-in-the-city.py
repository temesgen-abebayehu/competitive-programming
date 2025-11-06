class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # rains = [1,2,0,0,2,1] => (day-> lake)
        # create dict to traverse day with lake
        full = {}
        # create set to traverse dry day
        dry = []
        ans = [-1] * len(rains)

        for day, lake in enumerate(rains):
            # it is dry day
            if lake == 0:
                dry.append(day)
                continue
            
            # it should dry to avoide flood
            if lake in full:
                idx = bisect.bisect_right(dry, full[lake])
                if idx == len(dry):
                    return []

                ans[dry[idx]] = lake
                dry.pop(idx)

            # mark the lake already full
            full[lake] = day

        for day in dry:
            ans[day] = 1
        
        return ans      