class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # add the interval that before new interval to the result
        while i<n and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i+=1

        # merge overlaped interval
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1

        # append the merged interval
        result.append(newInterval)

        # append the remaining interval
        while i<n:
            result.append(intervals[i])
            i+=1
        
        return result
        