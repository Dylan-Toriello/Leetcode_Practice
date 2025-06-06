class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Initialize a dictionary
        res = defaultdict(list)
        #iterate through the list and add to the dictionary
        for num in nums:
        #increment keys as necessary
            res[num] = res.get(num, 0) + 1 
        
        #sort dictionary 
        sort_res = sorted(res.items(),  reverse = True)

        l = []
        #make a list and add the values
        for i in range(k):
            #adds the first element only
            l.append(sort_res[i][0])

        return l