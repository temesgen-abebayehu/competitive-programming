class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.is_end = True

        words = sentence.split(' ')

        ans = []
        for word in words:            
            curr = self.root
            dic = []
            flag = True

            for c in word:
                dic.append(c)
                if c not in curr.children:
                    flag = False
                    break
                    
                curr = curr.children[c]
                if curr.is_end:
                    break

            if flag:
                ans.append(''.join(dic))
            else:
                ans.append(word)

        return ' '.join(ans)
        