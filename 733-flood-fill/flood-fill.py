class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r_len = len(image)
        c_len = len(image[0])

        def in_bound(i, j):
            return 0 <= i < r_len and 0 <= j < c_len

        
        que = deque([[sr,sc]])
        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        orig_col = image[sr][sc]
        
        if image[sr][sc] == color:
            return image

        while que:
            r, c = que.popleft()
            image[r][c] = color
            for i, j in dir:
                if in_bound(r+i, c+j) and image[r+i][c+j] == orig_col:
                    que.append([r+i, c+j])
        return image