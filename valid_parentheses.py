class Solution:
    def isValid(self, s: str) -> bool:
   #make an empty stack

        #map a map of matching brackets

        #for each character in string:
            #if character is open bracket:
                #add to our stack
            #else if char is closing bracket
                #if stack empty or top stack is not partner of char:
                    #return false
                #else:
                    #remove top element from stack
        #return (stack is empty)

        def is_empty(stack):
            return len(stack) == 0
        
        stack = []

        charMap = {"(" : ")",
                "{" : "}",
                "[" : "]"}
        

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == "}" or char == "]" or char == ")":
                if is_empty(stack) or char !=  charMap[stack[-1]]   :
                    return False
                else:
                    stack.pop()
        return (is_empty(stack))