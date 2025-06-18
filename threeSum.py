class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #make the three pointer list and sort the numbers
        threePointerList = []
        nums.sort()

        #Get Index and value from list
        for index, val in enumerate(nums):
            #if val > 0 end program and return empty list since list is sorted if the current # is > 0 then there will be no point in continuing
            if val > 0:
                break

            # if the index is > 0 and val == nums[index -1] restart loop to avoid duplicate triplets
            if index > 0 and val == nums[index-1]:
                continue
            l, r = index + 1, len(nums)-1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum  < 0:
                    l +=1
                else:
                    threePointerList.append([val, nums[l], nums[r]])
                    #move both pointers to find next potential triplet
                    l+=1
                    r-=1
                    #skip duplicate values for the left pointer
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
        return threePointerList