class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # create stack
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            # assign start idx for extend the height
            start_idx = idx
            # if the top of stack is greater we just pop it
            while stack and stack[-1][1] > height:
                pre_idx, pre_height = stack.pop()

                # calculate the area
                max_area = max(max_area, pre_height * (idx - pre_idx))

                # extennd the stact idx
                start_idx = pre_idx

            stack.append((start_idx, height))
        
        idx += 1
        while stack:
            pre_idx, pre_height = stack.pop()

            # calculate the area
            max_area = max(max_area, pre_height * (idx - pre_idx))
            
        return max_area