class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Initialize a dictionary
        res = {}
        #iterate through the list and add to the dictionary
        for num in nums:
        #increment keys as necessary
            res[num] = res.get(num, 0) + 1 
        
        arr =[]
        for n, count in res.items():
            arr.append([count, n])
        arr.sort()

        resolution = []
        while len(resolution) <k:
            resolution.append(arr.pop()[1])

        return resolution