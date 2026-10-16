class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False
        
        dicts = {}

        for char in s :
            if char in dicts :
                dicts[char] += 1

            else :
                dicts[char] = 1


        dictt = {}

        for char in t :
            if char in dictt :
                dictt[char] +=1
            else :
                dictt[char] =1


        for key in dicts :
            if dicts[key] != dictt.get(key,0) :
                return False
        
        return True
        