class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        current_pairs = 0
        total = 0
        
        for right in range(len(nums)):
            current_pairs += freq[nums[right]]
            freq[nums[right]] += 1
            
            
            while current_pairs >= k:
                total += len(nums) - right
                freq[nums[left]] -= 1
                current_pairs -= freq[nums[left]]
                left += 1
        
        return total