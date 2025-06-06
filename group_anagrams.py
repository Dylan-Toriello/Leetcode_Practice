class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #go through the list and track the number of letters 
        #see which match and add them to the list 
        
        #intiliaze dictionary
        res = defaultdict(list)
        
        #go through the list of strings
        for s in strs:
        #make a list that keeps track of count (this sets all values = 0 w/ length of 26)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            #whatever key count provides is the list its going to get added to
            res[tuple(count)].append(s)
        return list(res.values())