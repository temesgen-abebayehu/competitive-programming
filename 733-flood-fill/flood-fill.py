class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r_len = len(image)
        c_len = len(image[0])

        def in_bound(i, j):
            return 0 <= i < r_len and 0 <= j < c_len

        visited = set()
        que = deque([[sr,sc]])
        dir = [[1,0], [0,1], [-1,0], [0,-1]]

        while que:
            r, c = que.popleft()
            for i, j in dir:
                if in_bound(r+i, c+j) and (r+i, c+j) not in visited and image[r+i][c+j] == image[r][c]:
                    que.append([r+i, c+j])
                    visited.add((r+i, c+j))
            image[r][c] = color
        return image