class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize an empty hash map
        #initialize max_length = 0

        #for each char in string and index of Right position:
            #if char in hashmap:
                # left_position = max(LP, hashmap[right position] + 1)

            #add to hashmap
            # max_length = max(max_length , RP - LP + 1)

        #return max_length

        char_index_map = {}

        lp = 0
        max_length = 0

        for RP, char in enumerate(s):
            if char in char_index_map:
                lp = max(lp, char_index_map[char] + 1)

            char_index_map[char] = RP
            max_length = max(max_length, RP - lp + 1)

        return max_length
