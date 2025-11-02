class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: List[str]) -> None:        
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            error = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    error += 1

                if error > 1:
                    break

            if error == 1:
                return True

        return False
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)