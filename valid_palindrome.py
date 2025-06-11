class Solution:
    def isPalindrome(self, s: str) -> bool:
         #convert string to lowercase and remove any non alphanumeric characters

        #set left pointer at index poissition 0
        # set right pointer at index position (len -1)
        # whle LP position is less than RP position:
            #if LP character is not eqaul to RP Character:
                #return false

                #move lp one position forwards 
                #move rp one position backward
        #return true
        st = ""
        for i in s:
            if i.isalnum():
                st += i
        
        
        st = st.lower()
        lp = 0
        rp = len(st) - 1

        while lp < rp:
            if st[lp] != st[rp]:
                return False
            lp += 1
            rp = rp - 1
        return True