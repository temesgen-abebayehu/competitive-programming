class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
            
        res = []
        for x,y in queries:
            res.append(arr[y] ^ (arr[x-1] if x>0 else 0))            

        return res