class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #make 2 points one at start and end
        #make an answer variable

        #while the left pointer < right pointer:
            #area = min(height at left pointer, height at right pointer) * width (right pointer - left pointer)
            #answer = max(answer, area)

            #if left pointer height <= right pointer height:
                #left pointer incremented by 1

            #else
                #right pointer decreased by 1

        #return answer



        start, end = 0, len(heights) - 1
        res = 0

        while start < end:
            #calculates the area include end - start index because index matters for area 
            area = min(heights[l], heights [r]) * (end - start)
            res - max (res, area)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r -=1
        return res
