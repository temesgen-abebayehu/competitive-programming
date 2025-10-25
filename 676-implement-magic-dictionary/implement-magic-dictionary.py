class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

    def search(self, searchWord: str) -> bool:
        def dfs(node, index, mismatch_used):
            if index == len(searchWord):
                return node.is_end and mismatch_used
            
            char = searchWord[index]
            
            # If we haven't used mismatch yet, try all possible characters
            if not mismatch_used:
                for child_char, child_node in node.children.items():
                    # If character matches, continue without using mismatch
                    if child_char == char:
                        if dfs(child_node, index + 1, False):
                            return True
                    else:
                        # Use mismatch for this position
                        if dfs(child_node, index + 1, True):
                            return True
            else:
                # Mismatch already used, must match exactly
                if char in node.children:
                    return dfs(node.children[char], index + 1, True)
            
            return False
        
        return dfs(self.root, 0, False)