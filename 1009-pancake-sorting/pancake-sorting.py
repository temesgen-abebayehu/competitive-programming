class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(a, k):
            return a[:k][::-1] + a[k:]

        result = []
        for i in range(len(arr), 0,-1):
            index = arr.index(i)

            if i != index + 1:
                if index != 0:
                    arr = flip(arr, index + 1)
                    result.append(index + 1)

                arr = flip(arr, i)
                result.append(i)

        return result