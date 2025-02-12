class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        person = defaultdict(int)
        for i in range(len(names)):
            person[heights[i]] = names[i]
        
        person = sorted(person.items(), reverse=True)
        return ([x[1] for x in person])
        