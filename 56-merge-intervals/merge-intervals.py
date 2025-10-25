class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the given intervals by start time min->max(asc)
        intervals.sort()
        
        # create variable that hold the result 
        result  = []

        # create a variable that holds start and end of non-overlap interval
        start = intervals[0][0]
        end = intervals[0][1]

        # create loop iterate to all interval to check if they are overlap      
        for curr_start, curr_end in intervals:
            # if overlap ocur we just merge them
            if end >= curr_start:
                end = max(end, curr_end)
            else:
                # we appended non-overlap interval
                result.append([start, end])
                start = curr_start
                end = curr_end

        # append the last interval
        result.append([start, end])

        return result 
            
            