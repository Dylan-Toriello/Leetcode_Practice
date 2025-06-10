class Solution:

    def encode(self, strs: List[str]) -> str:
        #make an empty string
        #iterate through the string list and concatenate into one string with a . between each string
        s = ""

        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        #make an empty list and index counter
        #While i < len(s):
        #j = i
        #while S[j] != #
        #length = int(s[i:j])
        # i = j +1
        #j = i + length
        #append to empty list
        #i = j

        #return list

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res