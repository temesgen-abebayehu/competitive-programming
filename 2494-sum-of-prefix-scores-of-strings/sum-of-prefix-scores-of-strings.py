class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # built trie node
        for word in words:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]
                curr.count += 1
                    
        # prifix score calculation
        ans = []
        for word in words:
            curr = self.root
            curr_ans = 0

            for char in word:
                if char in curr.children:
                    curr = curr.children[char]
                    curr_ans += curr.count

            ans.append(curr_ans)

        return ans