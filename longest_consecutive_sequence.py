class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #make a numset and a longestrun variable

        #go through the set checking if there isnt a previous number beforehand if so length = 1

        #while (num+ length) in numset:
            #length +=1
        #longest = max(longest, length)

        #return longest

        numset = set(nums)
        longestrun = 0

        for num in numset:
            if(num - 1) not in numset:
                length = 1
                while(num + length) in numset:
                    length += 1
                longestrun = max(length, longestrun)
        return longestrun
