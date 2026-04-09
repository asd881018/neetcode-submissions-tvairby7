class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # "act", "cat"
        # a: 1, c:1, t:1
        # find the same pattern of diff string
        # [{a:1, c:1, t:1}, {s:1, t:1, o:1, p:1}, {a:1, h:1, t:1} ]
        # index: 0, 1, 2
        # another array to store the actual string

        res = defaultdict(list) # mapping the charCount to list of anagrams

        for str in strs:
            count = [0] * 26 

            for c in str:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(str)

        return res.values()