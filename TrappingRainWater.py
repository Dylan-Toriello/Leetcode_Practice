class Solution:
    def trap(self, height: List[int]) -> int:
        #pointer at the front and back

        #left side max right side max

        #while l < r:
            #if leftside , rightside:
            # l+=1
            #leftmax = max(leftmax, height[l])
            #res += leftmax - height[l]

            #else:
                #r -=1
                #rightmax = max(rightmax, height[right])
                #res += rightmax - height[r]

        #return res

        l, r = 0, len(height) - 1

        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height [r]:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res 