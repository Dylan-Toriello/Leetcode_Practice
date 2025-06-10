class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #make variables keeping track of product and zero count
        #iterate over list of nums to keep track of product and zero count
        #if zerocount > 1 return the whole list as zeros
        #make a list with all zeros
        #iterate through nums keeping track of index and value
        #if zerocount > 0 then you check if it is zero and if it isn't putting zero if its not the index containing zero and product if it is the index containing zero
        #else product // value

        prod, zeroCount = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zeroCount +=1

        if zeroCount > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for index, val in enumerate(nums):
            if zeroCount > 0:
                if val != 0:
                    res[index] = 0
                else:
                    res[index] = prod
            else:
                res[index] = prod // val
        return res